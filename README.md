# BNS Legal Research RAG Chatbot



This project implements a Retrieval-Augmented Generation (RAG) chatbot over the Bharatiya Nyaya Sanhita (BNS).



## Features

- RAG pipeline over legal documents

- Local vector database (Chroma)

- Sentence-transformer embeddings

- Open-weight LLM (Qwen2-0.5B)

- Streamlit interface



## Architecture

PDF → Chunking → Embeddings → Vector DB → Retriever → LLM → Answer



## Run locally



Install dependencies:



pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers transformers streamlit



Run the chatbot:



streamlit run app.py



## Example queries



- What is punishment for murder under BNS?

\- Difference between murder and culpable homicide?

\- Punishment for theft under BNS?

