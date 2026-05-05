from langchain_community.vectorstores import Chroma

def create_vector_db(chunks, embeddings):
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory="chroma_db"
        )
    
    db.persist()
    return db

def load_vector_db(embeddings):
    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
