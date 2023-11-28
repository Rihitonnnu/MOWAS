# 環境変数の準備
from langchain import OpenAI, SerpAPIWrapper, LLMChain
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor, load_tools
import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


def search_spot():
    # ツールの準備
    tools = load_tools(["google-search"], llm=ChatOpenAI())

    # プロンプトテンプレートの準備
    prefix = """次の質問にできる限り答えてください。次のツールにアクセスできます:"""
    suffix = """始めましょう! 

    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools,
        prefix=prefix,
        suffix=suffix,
        input_variables=["input", "agent_scratchpad"]
    )

    # エージェントの準備
    llm_chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools)
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=tools, verbose=True)

    agent_executor.run("福岡県福岡市西区のカフェを一つ教えて")
