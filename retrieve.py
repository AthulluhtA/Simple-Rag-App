from langchain.tools import tool
from ingest import vector_db

current_hash = None

@tool
def retrieved(query:str):
    """Retrieve information to answer a query"""
    print(f"current_hash is: {current_hash}")
    retrieved_docs = vector_db.similarity_search(query, 
                                                 filter={'source_hash': current_hash},
                                                 k=3)
    serialized = "\n\n".join(
        (f"source:{doc.metadata}\nContent:{doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs