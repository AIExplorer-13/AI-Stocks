from loaders.pdf_loader import load_pdf
from loaders.txt_loader import load_txt

from processing.chunker import chunk_docs

from processing.embeddings import get_embeddings

from vectordb.db import create_vector_db

from retrieval.retriever import get_retriever

from agent.agent import run_agent

# LOAD DATA
docs = []

docs += load_pdf(r"C:\Users\vidya\OneDrive\Pictures\Documents\Stock_RAG\rag_data\rag_data_txt\zerodha-stocks-basics.pdf")

docs += load_pdf(r"C:\Users\vidya\OneDrive\Pictures\Documents\Stock_RAG\rag_data\rag_data_txt\zerodha-Fundamental Analysis.pdf")

docs += load_txt("data/raw/structured_txt/ratios.txt")

# CHUNK
chunks = chunk_docs(docs)

# EMBEDDINGS
embeddings = get_embeddings()

# DB
db = create_vector_db(chunks, embeddings)

# RETRIEVER
retriever = get_retriever(db)

# CHAT LOOP
while True:

    query = input("\nAsk Question: ")

    response = run_agent(query, retriever)

    print("\nAI Answer:\n")

    print(response)