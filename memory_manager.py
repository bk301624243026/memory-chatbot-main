import json
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from config import load_llm

llm = load_llm()

buffer_memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

summary_memory = ConversationSummaryMemory(
    llm=llm,
    memory_key="chat_history"
)

def reset_memory():
    buffer_memory.clear()
    summary_memory.clear()
    print("Memory Reset Successful")

def save_memory():
    data = buffer_memory.chat_memory.messages
    with open("chat_history.json", "w") as f:
        json.dump([str(i) for i in data], f)
    print("Memory Saved")

def load_memory():
    try:
        with open("chat_history.json", "r") as f:
            data = json.load(f)
            print("Loaded Memory:", data)
    except:
        print("No saved memory")
