import pprint
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# APIのエンドポイントURL
url = "https://places.googleapis.com/v1/places:searchNearby"

# リクエストボディ
payload = {
    "includedTypes": ["cafe"],
    "maxResultCount": 1,
    "locationRestriction": {
        "circle": {
            "center": {
                "latitude": 33.5895,
                "longitude": 130.3197},
            "radius": 500.0
        }
    }
}

# ヘッダー
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': os.environ["GOOGLE_API_KEY"],  # 実際のAPIキーに置き換えてください
    'X-Goog-FieldMask': 'places.displayName',
    'Accept-Language': 'ja'  # 日本語での結果を得るために追加
}

# POSTリクエストを実行
response = requests.post(url, headers=headers, data=json.dumps(payload))

# レスポンスのJSONを取得
data = response.json()

# 結果を表示（pprintモジュールを使用して見やすく表示）
pprint.pprint(data)
