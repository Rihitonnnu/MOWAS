import openai
import os

import json
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

index = []

options = ['眠い', '眠くない', '少し眠い', '眠くなりかけている']
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
