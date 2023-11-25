from langchain.utilities import GoogleSearchAPIWrapper
import openai
from dotenv import load_dotenv
load_dotenv()

# langchainからGoogleSearchAPIのみを使う場合
search = GoogleSearchAPIWrapper()
result = search.run("明日の福岡の天気を教えて")

print(result)
