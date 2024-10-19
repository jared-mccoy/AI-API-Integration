A Hands-on Guide to Real-Time AI API Integrations

Welcome to this interactive course on AI API integrations! This course is designed to provide you with hands-on experience working with cutting-edge AI services through their APIs.

## Modules

1. [Building Custom Models with OpenAI GPT API](../modules/modules/01_gpt_api/README.md)
2. (More modules to come)

## Getting Started

This course offers two ways to engage with the material:

### 1. View Lessons Online

You can view all lesson content directly on GitHub or our GitHub Pages site. This is the quickest way to access the course material, but it won't allow for interactive coding.

### 2. Interactive Coding

For a hands-on experience, you have two options:

#### A. Use Google Colab (Recommended for Beginners)

Click the "Open in Colab" badge at the beginning of each notebook to launch an interactive environment.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jared-mccoy/AI-API-Integration-Course/blob/main/modules/01_gpt_api/01_gpt_api_intro.ipynb)

**API Key Security in Colab:**
- You'll be prompted to enter your API key manually.
- This is safe for educational purposes, but remember:
  - Never save the notebook with your API key visible.
  - Clear output cells containing the key before saving or sharing.
  - You can delete/regenerate your API key after the course for peace of mind.

#### B. Clone the Repository (For Advanced Users)

1. Clone this repository to your local machine.
2. Set up a virtual environment and install requirements:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Start Jupyter Notebook: `jupyter notebook`

This method provides the most control but requires more setup.

## API Key Management

- Always keep your API keys confidential.
- If you suspect your key has been compromised, or just for peace of mind after the course:
  1. Go to your OpenAI account dashboard.
  2. Find the exposed key and click "Revoke".
  3. Generate a new key if needed.

## Requirements

All necessary Python packages are listed in `requirements.txt`.

Happy learning!
