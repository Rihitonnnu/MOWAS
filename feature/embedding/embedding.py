import json
import openai
import numpy as np


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def embedding(input):
    with open('json/index.json') as f:
        INDEX = json.load(f)

    # 入力を複数にしてqueryを用意してコサイン類似度を用いて検索させる
    query = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=input
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
    sleepy_result = {
        '眠い': 'sleepy',
        '少し眠い': 'sleepy',
        '眠くなりかけている': 'sleepy',
        '眠くない': 'notsleepy',
    }

    # 現在眠いか眠くないかを出力
    print(sleepy_result[results[0]["body"]])
    # print(f'一番近い文章は {results[0]["body"]} です')
