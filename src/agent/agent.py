from langchain_core.prompts import PromptTemplate
from llm.model import get_llm 

llm = get_llm()

template = """
You are a financial AI assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{question}

Instructions:
- Use financial reasoning
- Use formulas if needed
- Use rules from context
- Be concise and structured

Answer:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

def run_agent(query, retriever):

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    final_prompt = prompt.format(
        context=context,
        question=query
    )

    response = llm.invoke(final_prompt)

    return response