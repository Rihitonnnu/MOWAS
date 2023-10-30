from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
import openai
from langchain.agents import load_tools

import os
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper


from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
os.environ["GOOGLE_API_KEY"]
os.environ["GOOGLE_CSE_ID"] = "30a361b9d5d85489b"

# search = GoogleSearchAPIWrapper()

# tool = Tool(
#     name="Google Search",
#     description="Search Google for recent results.",
#     func=search.run,
# )

# tool.run("Obama's first name?")
llm = OpenAI(temperature=0)
tool_names = ["google-search"]
tools = load_tools(tool_names, llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("""
現在の日本の総理大臣は誰ですか？
""")
