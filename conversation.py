import os
import logging
from dotenv import load_dotenv

import openai

logging.basicConfig(filename='Log.txt', filemode='w', level=logging.DEBUG)
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

# 標準入力と改行
userSpeech = input()
print()

# 終了するまで無限に続ける
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": userSpeech},
    ],
)

# レスポンスを表示
print(response.choices[0]["message"]["content"].strip())
