# RAG Document Assistant

A conversational AI assistant that lets you upload any PDF and ask questions about it.
Built with LangChain, Groq (Llama 3.1 8B), Google Generative AI Embeddings, ChromaDB, and Streamlit.

## Features

- Upload any PDF and query it in natural language
- Conversational chat interface
- Powered by Llama 3.1 8B via Groq
- Fully containerized with Docker

## Tech Stack

- **LLM:** Llama 3.1 8B Instruct (Groq)
- **Embeddings:** Google Generative AI (gemini-embedding-001)
- **Vector DB:** ChromaDB
- **Framework:** LangChain
- **UI:** Streamlit

## Setup

### Prerequisites
- Docker
- Groq API key — [console.groq.com](https://console.groq.com)
- Google API key — [aistudio.google.com](https://aistudio.google.com)

### Run with Docker

1. Clone the repo
```bash
   git clone https://github.com/AthulluhtA/Simple-Rag-App.git
   cd Simple-Rag_App
```

2. Create a `.env` file
```
    GROQ_API_KEY=your_groq_api_key
    GOOGLE_API_KEY=your_google_api_key
```

3. Build and run
```bash
   docker build -t rag-app .
   docker run --env-file .env -p 8501:8501 rag-app
```

4. Open `http://localhost:8501` in your browser

### Run locally (without Docker)

1. Install dependencies
```bash
   pip install -r requirements.txt
```

2. Run the app
```bash
   streamlit run app.py
```

## Project Structure
```
├── ingest.py        # PDF loading, chunking, embedding
├── retrieve.py      # Vector DB retrieval tool
├── agent.py         # LLM agent setup
├── app.py           # Streamlit UI
├── Dockerfile
└── requirements.txt
```