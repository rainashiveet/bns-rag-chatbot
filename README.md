# BNS Legal Research RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot over the **Bharatiya Nyaya Sanhita (BNS)**.  
The system allows users to ask legal questions and retrieves the most relevant sections of the law before generating an answer using an open-weight language model.

The goal of the system is to provide **accurate, grounded legal responses** by combining semantic retrieval with an open-source LLM.

---

## Features

- Retrieval-Augmented Generation (RAG) pipeline over legal documents
- Local vector database using **ChromaDB**
- Semantic embeddings using **Sentence Transformers**
- Open-weight LLM (**Qwen2-0.5B**) for answer generation
- **Streamlit-based interactive interface**
- Supports questions that span multiple legal sections

---

## Architecture

The system follows a standard **RAG architecture**:


PDF Documents → Chunking → Embeddings → Vector Database → Retriever → LLM → Answer


1. Legal documents are loaded from PDF.
2. Documents are split into smaller chunks.
3. Each chunk is converted into embeddings.
4. Embeddings are stored in a **Chroma vector database**.
5. When a user asks a question:
   - The system retrieves the most relevant legal sections.
   - The retrieved context is passed to the LLM.
6. The LLM generates an answer grounded in the retrieved legal context.

---

## Chunking Strategy

Legal documents are split using **RecursiveCharacterTextSplitter** with:

- **Chunk size:** 500
- **Chunk overlap:** 50

This strategy ensures that legal clauses remain semantically meaningful while improving retrieval accuracy.

---

## Retrieval Strategy

The system performs **similarity search over ChromaDB** to retrieve the **top-4 most relevant chunks** for a given query.

Retrieving multiple chunks allows the chatbot to answer questions that span **multiple sections of the Bharatiya Nyaya Sanhita**.

---

## Model

Generation is performed using the open-weight model:

**Qwen2-0.5B**

The model is loaded using **HuggingFace Transformers** and generates responses based on the retrieved legal context.

---

## Run Locally

Install dependencies:

pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers transformers streamlit accelerate


Run the chatbot:

streamlit run app.py


---

## Example Queries

Example questions the system can answer:

- What is punishment for murder under BNS?
- What is the difference between murder and culpable homicide?
- What is the punishment for theft under BNS?
- What are the legal consequences of criminal intimidation?

---

## Tech Stack

- **Python**
- **LangChain**
- **ChromaDB**
- **Sentence Transformers**
- **HuggingFace Transformers**
- **Streamlit**

---

## Repository

GitHub Repository:  
https://github.com/rainashiveet/bns-rag-chatbot

---

## Author

Shiveet Raina


