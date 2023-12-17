import json
import openai
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def load_index():
    with open('../json/embedding/introduce_reaction.json') as f:
        return json.load(f)


def calculate_similarity(query, index):
    results = map(
        lambda i: {
            'body': i['body'],
            'similarity': cosine_similarity(i['embedding'], query)
        },
        index
    )
    return sorted(results, key=lambda i: i['similarity'], reverse=True)


def get_sleepy_result():
    return {
        '眠い': 'sleepy',
        '少し眠い': 'sleepy',
        '眠くなりかけている': 'sleepy',
        '眠くない': 'notsleepy',
    }


def embedding(input):
    index = load_index()

    query = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=input
    )

    query = query['data'][0]['embedding']

    results = calculate_similarity(query, index)

    # sleepy_result = get_sleepy_result()
    introduce_reaction_result = {
        'はい': 'good',
        'いいえ': 'bad',
        'してください': 'good',
        'しないでください': 'bad'
    }

    # print(sleepy_result[results[0]["body"]])
    print(introduce_reaction_result[results[0]["body"]])
    # print(f'一番近い文章は {results[0]["body"]} です')


embedding('案内しないで')
