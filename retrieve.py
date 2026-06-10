from langchain.tools import tool
from ingest import vector_db

@tool
def retrieved(query:str):
    """Retrieve information to answer a query"""
    retrieved_docs = vector_db.similarity_search(query, k=3)
    serialized = "\n\n".join(
        (f"source:{doc.metadata}\nContent:{doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs