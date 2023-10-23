import openai
import os

import json
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

index = []

options = ['会話終了', '会話開始', '周辺情報の教示', '眠気を示す指標の教示']
for option in options:
    res = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=option,
    )
    index.append({
        'body': option,
        'embedding': res['data'][0]['embedding']
    })

with open('index.json', 'w') as f:
    json.dump(index, f)
