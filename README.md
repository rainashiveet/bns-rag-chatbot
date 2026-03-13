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


## Chunking Strategy

Legal documents are split using a RecursiveCharacterTextSplitter with chunk size 500 and overlap 50.  
This ensures legal clauses remain semantically meaningful while improving retrieval accuracy.

## Retrieval Strategy

The system uses similarity search over ChromaDB to retrieve the top-4 most relevant chunks for a user query.

This allows the chatbot to answer questions that span multiple sections of the Bharatiya Nyaya Sanhita.

## Model

Generation is performed using the open-weight model Qwen2-0.5B from HuggingFace.




## Example queries



- What is punishment for murder under BNS?

\- Difference between murder and culpable homicide?

\- Punishment for theft under BNS?

