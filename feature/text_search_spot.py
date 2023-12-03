import pprint
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# APIのエンドポイントURL
url = 'https://places.googleapis.com/v1/places:searchText'

# リクエストボディ
payload = {
    'textQuery': '福岡県福岡市西区西都のカフェ',
    'maxResultCount': 2
}

# ヘッダー情報
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': os.environ["GOOGLE_API_KEY"],  # あなたのGoogle APIキー
    'X-Goog-FieldMask': 'places.displayName,places.formattedAddress,places.priceLevel',
    'Accept-Language': 'ja'  # 日本語での結果を得るために追加

}

# POSTリクエストを実行
response = requests.post(url, json=payload, headers=headers)

# レスポンスのJSONを取得
data = response.json()

# 結果を表示
pprint.pprint(data)

# 検索結果がなかった場合の例外処理を入れておく必要がある
