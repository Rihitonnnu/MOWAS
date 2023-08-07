import os
import logging
from dotenv import load_dotenv

import openai

logging.basicConfig(filename='Log.txt', filemode='w', level=logging.DEBUG)
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


# 終了するまで無限に続ける

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "大谷翔平は今何歳ですか？"},
    ],
)

# レスポンスを表示
print(response.choices[0]["message"]["content"].strip())
