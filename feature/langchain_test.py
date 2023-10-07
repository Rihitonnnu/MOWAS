from langchain.memory import ConversationBufferMemory
# LLM のラッパーをインポート
from langchain.llms import OpenAI
# チェーンクラスをインポート
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv
load_dotenv()

# メモリの初期化
memory = ConversationBufferMemory()

# LLM の初期化
llm = OpenAI(temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"])

# チェーンの初期化（使用する LLM と メモリオブジェクトを渡す）
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# 会話を開始
user_input = input("You: ")

while True:
    response = conversation.predict(input=user_input)
    print(f"AI: {response}")
    user_input = input("You: ")
    if user_input == "exit":
        break
