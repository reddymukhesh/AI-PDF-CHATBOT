# AI PDF Chatbot using RAG and TinyLlama

## Overview

This project is an AI-powered PDF chatbot built using Generative AI, Retrieval-Augmented Generation (RAG), LangChain, Ollama, TinyLlama, FAISS, and Streamlit.

The chatbot allows users to upload PDF documents and ask questions based on document content using semantic search and local Large Language Models.

---

## Features

* Upload PDF documents
* Extract text from PDFs
* Semantic chunking
* Embedding generation
* Vector similarity search using FAISS
* Local LLM inference using TinyLlama
* Streamlit-based interactive UI
* Fully offline AI workflow

---

## Technologies Used

* Python
* Streamlit
* LangChain
* Ollama
* TinyLlama
* FAISS
* PyPDF
* nomic-embed-text

---

## Workflow

1. Upload PDF
2. Extract text
3. Split text into chunks
4. Generate embeddings
5. Store vectors in FAISS
6. Perform semantic search
7. Generate answers using TinyLlama

---

## Installation In Terminal


pip install -r requirements.txt


Install Ollama:

https://ollama.com

Pull required models:


ollama pull tinyllama
ollama pull nomic-embed-text

Run project:


streamlit run app.py

## Future Improvements

* Multiple PDF support
* Conversation memory
* OCR support
* Source citations
* Voice assistant
* Cloud deployment


## Author

Mukhesh Reddy
