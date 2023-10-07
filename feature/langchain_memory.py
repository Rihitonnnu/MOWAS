# from langchain.memory import ConversationBufferMemory

# memory = ConversationBufferMemory()
# memory.chat_memory.add_user_message("hi!")
# memory.chat_memory.add_ai_message("what's up?")

# print(memory.load_memory_variables({}))

from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import os

template = """あなたの名前はもわすです。
{history}
Human: {human_input}
MOWAS:"""
prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"]),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)

output = chatgpt_chain.predict(human_input="こんにちは")
print(output)
