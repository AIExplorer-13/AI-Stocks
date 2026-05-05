from langchain_community.document_loaders import PyMuPDFLoader

path = r"C:\Users\vidya\OneDrive\Pictures\Documents\Stock_RAG\rag_data\rag_data_txt\zerodha-Fundamental Analysis.pdf"
def load_pdf(path):
    loader = PyMuPDFLoader(path)
    return loader.load()

if __name__ == "__main__":
    documents = load_pdf(path)
    print(documents[10].page_content)