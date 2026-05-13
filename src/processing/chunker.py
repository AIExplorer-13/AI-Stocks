from langchain_text_splitters import RecursiveCharacterTextSplitter

def detect_type(text):

    if "[RULE]" in text:
        return "rule"

    elif "[FORMULA]" in text:
        return "formula"

    elif "[CONCEPT]" in text:
        return "concept"

    elif "[INSIGHT]" in text:
        return "insight"

    elif "[TABLE_ROW]" in text:
        return "table"

    else:
        return "general"


def chunk_docs(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )

    chunks = splitter.split_documents(documents)

    for chunk in chunks:
        chunk.metadata["type"] = detect_type(chunk.page_content)

    return chunks