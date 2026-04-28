from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from config import load_llm
from memory_manager import buffer_memory, summary_memory, reset_memory, save_memory
from logger import log

llm = load_llm()

template = """
You are a helpful AI chatbot.

Chat History:
{chat_history}

User:
{input}

AI:
"""

prompt = PromptTemplate(
    input_variables=["chat_history", "input"],
    template=template
)

buffer_chain = ConversationChain(
    llm=llm,
    memory=buffer_memory,
    prompt=prompt
)

summary_chain = ConversationChain(
    llm=llm,
    memory=summary_memory,
    prompt=prompt
)

def token_count():
    return len(str(buffer_memory.chat_memory.messages))

while True:
    try:
        user = input("\nYou: ")

        if user.lower() == "exit":
            save_memory()
            print("Memory saved. Exiting.")
            break

        if user.lower() == "reset":
            reset_memory()
            continue

        print("\nBUFFER MEMORY RESPONSE:")
        response1 = buffer_chain.predict(input=user)
        print(response1)

        print("\nSUMMARY MEMORY RESPONSE:")
        response2 = summary_chain.predict(input=user)
        print(response2)

        print("\nToken Growth:", token_count())

        log(user)

    except Exception as e:
        print("Error:", e)
        log(str(e))
