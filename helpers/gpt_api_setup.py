import importlib.util
import subprocess
import sys
import os
from getpass import getpass

# Global variable to store the client
_client = None

def check_openai_installed():
    if importlib.util.find_spec("openai") is None:
        print("OpenAI package not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
        print("OpenAI package installed successfully.")
    else:
        print("OpenAI package is already installed.")

def import_openai():
    check_openai_installed()
    global OpenAI
    from openai import OpenAI

def validate_api_key(api_key):
    try:
        client = OpenAI(api_key=api_key)
        # Make a simple API call to test the key
        client.models.list()
        return True
    except Exception as e:
        print(f"Error validating API key: {str(e)}")
        return False

def get_api_key():
    while True:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("OPENAI_API_KEY not found in environment variables.")
            api_key = getpass("Please enter your OpenAI API key: ")
        
        if validate_api_key(api_key):
            os.environ["OPENAI_API_KEY"] = api_key
            return api_key
        else:
            print("Invalid API key. Please try again.")
            os.environ.pop("OPENAI_API_KEY", None)  # Remove the invalid key from env

def setup_openai_client():
    global _client
    import_openai()

    api_key = get_api_key()

    # Initialize the OpenAI client
    _client = OpenAI(api_key=api_key)

    print(f"API Key set: {'Yes' if _client.api_key else 'No'}")
    print(f"API Key (first 5 chars): {_client.api_key[:5] if _client.api_key else 'None'}")

    return _client

def get_completion(prompt, model="gpt-3.5-turbo"):
    global _client
    if _client is None:
        _client = setup_openai_client()
    messages = [{"role": "user", "content": prompt}]
    response = _client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content