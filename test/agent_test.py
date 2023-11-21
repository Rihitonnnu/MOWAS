import openai
from dotenv import load_dotenv
load_dotenv()

# langchainからGoogleSearchAPIのみを使う場合
from langchain.utilities import GoogleSearchAPIWrapper
search = GoogleSearchAPIWrapper()
search.run("high temperature SF yesterday Fahrenheit")
