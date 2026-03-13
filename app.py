import streamlit as st
from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


# -------- Paths -------- #

PROJECT_DIR = Path(__file__).parent
VECTOR_DB_DIR = PROJECT_DIR / "vector_db"


# -------- Load Vector Database -------- #

@st.cache_resource
def load_vector_db():

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embedding_model,
        collection_name="bns_collection"
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k":3})

    return retriever


retriever = load_vector_db()


# -------- Load LLM -------- #

@st.cache_resource
def load_model():

    model_name = "Qwen/Qwen2-0.5B-Instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float32
    )

    return tokenizer, model


tokenizer, model = load_model()


# -------- RAG Answer Function -------- #

def ask_bns(question):

    docs = retriever.invoke(question)

    # smaller context = faster prompt
    context = "\n\n".join([
        d.page_content[:250] for d in docs
    ])

    prompt = f"""
You are a legal assistant for Bharatiya Nyaya Sanhita (BNS).

Answer clearly using the provided legal context.
Limit your answer to 3–4 complete sentences.

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=90,
        do_sample=False,
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    answer = generated_text.split("Answer:")[-1].strip()

    # ensure sentence ends cleanly
    if not answer.endswith("."):
        answer += "."

    return answer


# -------- Streamlit UI -------- #

st.title("⚖️ BNS Legal Research Chatbot")

st.write("Ask questions about Bharatiya Nyaya Sanhita (BNS).")

question = st.text_input("Ask a legal question:")

if question:

    with st.spinner("Searching relevant law sections..."):

        answer = ask_bns(question)

    st.write("### Answer")
    st.write(answer)