from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import pypdf
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')

vector_db = Chroma(
    collection_name='RAG_collection',
    embedding_function=embeddings,
    persist_directory='./langchain_vectordb',
)

def load_pdf(file_path: str) -> list[Document]:
    reader = pypdf.PdfReader(file_path)
    return [
        Document(
            page_content=page.extract_text() or "",
            metadata={"source": file_path, "page": i}
        )
        for i, page in enumerate(reader.pages)
    ]

def ingest(file_path: str):
    docs = load_pdf(file_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    split_docs = splitter.split_documents(docs)
    ids = vector_db.add_documents(documents=split_docs)
    print(f"Ingested {len(ids)} chunks from {file_path}")
    return vector_db