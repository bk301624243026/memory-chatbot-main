from langchain_ollama import ChatOllama

def load_llm():

    llm = ChatOllama(
        model="llama3",
        temperature=0.7
    )

    return llm
