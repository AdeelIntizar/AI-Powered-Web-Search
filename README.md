#  AI Research Assistant

A Streamlit-based AI research tool that searches across arXiv, Wikipedia, and the web using Groq's LLM models.

## Features

- Multi-source search (arXiv, Wikipedia, Web)
- Multiple AI models (Gemma2, Llama3, Mixtral)
- Real-time chat interface
- Customizable search sources

## Installation

```bash
git clone https://github.com/AdeelIntizar/AI-Powered-Web-Search.git
cd AI-Powered-Web-Search
pip install -r requirements.txt
streamlit run app.py
```

## Setup

1. Get your Groq API key from [console.groq.com](https://console.groq.com/)
2. Enter the API key in the sidebar when running the app

## Usage

1. Choose an AI model
2. Ask research questions in the chat



## Requirements

- Python 3.8+
- Groq API key
- Dependencies in `requirements.txt`

## Tech Stack

- **Frontend**: Streamlit
- **AI**: LangChain + Groq
- **Search**: arXiv API, Wikipedia API, DuckDuckGo

