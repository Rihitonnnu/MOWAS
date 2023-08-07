import os
import logging

import openai
from dotenv import load_dotenv

logging.basicConfig(filename='Log.txt', filemode='w', level=logging.DEBUG)
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "大谷翔平は今何歳ですか？"},
    ],
)

# レスポンスを表示
print(response.choices[0]["message"]["content"].strip())
