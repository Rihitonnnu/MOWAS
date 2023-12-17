import openai
import os

import json
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

index = []

options = ['はい', 'いいえ', 'してください', 'しないでください']
for option in options:
    res = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=option,
    )
    index.append({
        'body': option,
        'embedding': res['data'][0]['embedding']
    })

with open('introduce_reaction.json', 'w') as f:
    json.dump(index, f)
