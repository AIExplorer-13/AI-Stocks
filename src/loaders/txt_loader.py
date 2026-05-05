from langchain_core.documents import Document

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return [Document(page_content=content)]