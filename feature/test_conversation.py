import os
import logging
from dotenv import load_dotenv
import openai
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from langchain.chat_models import ChatOpenAI
import logging
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

logger = logging.getLogger(__name__)
logger.setLevel(10)
sh = logging.StreamHandler()
logger.addHandler(sh)
fh = logging.FileHandler('../log/conversation.log', encoding='utf-8')
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


template = """あなたはドライバーの覚醒を維持するシステムであり、名前はもわすです。自分の名前を呼ぶときはもわすと呼んでください。
まずユーザーに名前を聞いて下さい。
{chat_history}
Human: {human_input}
"""

human_template = "{text}"

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm = ChatOpenAI(temperature=0.1)
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

response = llm_chain.predict(human_input='こんにちは。あなたのお名前はなんですか？')
print(response)

human_input = input("You: ")

while True:
    try:
        response = llm_chain.predict(human_input=human_input)
        print(response)
        human_input = input("You: ")
        if human_input == "exit":
            break
    except KeyboardInterrupt:
        exit(1)
