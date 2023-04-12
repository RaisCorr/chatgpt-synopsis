# ChatGPT-Synopsis
This is a repository for a ChatGPT application that uses OpenAI's API and Replicate's API for generating text responses based on input prompts. It also uses VOICEVOX for text-to-speech synthesis.

## Preparation
To get started, clone the repository by running the following command in your terminal:

```
git clone https://github.com/RaisCorr/chatgpt-synopsis.git
```

## Installation
You can install the necessary libraries using Poetry by running the command:

```
poetry install
```

If you prefer to use pip, you can install the libraries by running the following command:
```
pip install -r requirements.txt
```

## API Key Registration
To use this application, you will need to obtain two API keys: OPENAI_API_KEY and REPLICATE_API_TOKEN.  
Once you have obtained the API keys, register them as environment variables on your local machine.

## Running VOICEVOX Speech Synthesis Engine
Before running the application, ensure that the VOICEVOX speech synthesis engine is running and a local HTTP server has been set up.

## Running the Application
To run the application, navigate to the root directory of the cloned repository and run the following command:
```
streamlit run main.py
```

This will start the Streamlit app and open it in your default web browser. You can now interact with the ChatGPT application in the browser.