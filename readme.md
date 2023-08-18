# <<<<<<< HEAD

> > > > > > > 1c756bbef4f0010aa7f6648c88ab2b58543561ee

## Ask Questions About Uploaded Articles

This Python application allows you to load a PDF and utilize natural language to inquire about its contents. The app employs a Language Learning Model (LLM) to generate responses based on the PDF's content. It's important to note that the LLM exclusively addresses questions pertaining to the document.

## How it Operates

The app reads the PDF, segmenting its text into manageable sections suitable for processing by the LLM. OpenAI embeddings craft vector representations of these segments. The app then identifies segments semantically relevant to the user's query and employs the LLM to generate responses.

Streamlit constructs the GUI, while Langchain interfaces with the LLM.

## Installation

Clone the repository and install prerequisites.

Don't forget to include your OpenAI API key in the `.env` file.

## Usage

Execute the app using the Streamlit CLI:

```bash
streamlit run app.py
```
