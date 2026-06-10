import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from retrieve import retrieved
import logging
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    api_key=os.getenv('GROQ_API_KEY')
    )



tools = [retrieved]
prompt = """You are a research assistant specialized in answering questions about academic papers.

You have access to a retrieval tool that fetches relevant sections from research papers.
Always use the tool before answering — never answer from memory alone.

Guidelines:
- Answer based strictly on the retrieved content
- If the context doesn't contain enough information, say "I don't have enough information in the provided papers to answer this"
- Cite the source and page number when possible
- Keep answers clear and precise — avoid unnecessary elaboration
- If asked to explain a concept, use the paper's own explanation first, then simplify if needed
- Never hallucinate citations, authors, or results
"""

doc_agent = create_agent(llm, tools, system_prompt=prompt)

def run_query(query:str) -> str:
    response = ""
    for chunk in doc_agent.stream({
        "messages":[{"role": "user", "content": query}]},
        stream_mode='values'
    ):
        last = chunk['messages'][-1]
        if last.type == "ai" and last.content:
            yield last.content