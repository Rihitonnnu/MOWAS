import numpy as np
import json
import os
import openai
from dotenv import load_dotenv
load_dotenv()


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


openai.api_key = os.environ["OPENAI_API_KEY"]

with open('index.json') as f:
    INDEX = json.load(f)

QUERY = "今自分はどのくらい眠い？"

# 入力を複数にしてqueryを用意してコサイン類似度を用いて検索させる
query = openai.Embedding.create(
    model='text-embedding-ada-002',
    input=QUERY
)

query = query['data'][0]['embedding']

results = map(
    lambda i: {
        'body': i['body'],
        # ここでクエリと各文章のコサイン類似度を計算
        'similarity': cosine_similarity(i['embedding'], query)
    },
    INDEX
)
# コサイン類似度で降順（大きい順）にソート
results = sorted(results, key=lambda i: i['similarity'], reverse=True)

# 類似性の高い選択肢を出力
print(f'一番近い文章は {results[0]["body"]} です')
