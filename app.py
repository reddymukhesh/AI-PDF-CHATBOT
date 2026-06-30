import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
# Load TinyLlama
llm = OllamaLLM( model="tinyllama")
# Page settings
st.set_page_config(page_title="AI PDF Chatbot")

# Title
st.title("AI PDF Chatbot")

st.write("Upload a PDF and ask questions from the document.")

# Upload PDF
pdf = st.file_uploader("Upload PDF", type="pdf")

# Run only if PDF uploaded
if pdf is not None:

    # Read PDF
    pdf_reader = PdfReader(pdf)

    text = ""

    # Extract text
    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)

    # Embedding model
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Create vector DB
    vector_store = FAISS.from_texts(
        chunks,
        embeddings
    )

    # QUESTION INPUT BOX
    user_question = st.text_input(
        "Ask a question from PDF"
    )

    # If user asks question
    if user_question.strip() != "":

        # Similarity search
        docs = vector_store.similarity_search(
            user_question
        )

        # Combine context
        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        # Prompt
        prompt = f"""
        Answer the question based on the context below.

        Context:
        {context}

        Question:
        {user_question}
        """

        

        # Generate response
        response = llm.invoke(prompt)

        # Display answer
        st.subheader("Answer")

        st.write(response)

else:
    st.info("Please upload a PDF first.")

