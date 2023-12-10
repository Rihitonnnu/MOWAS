import pprint
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


class TextSearchSpot:
    def __init__(self) -> None:
        pass

    # 住所を逆エンコードする(少し精度悪め)
    def reverse_geocoder():
        # Yahoo!リバースジオコーダAPIのURL
        url = "https://map.yahooapis.jp/geocode/V1/geoCoder"

        # いずれは関数として使ってあげたい

        # APIキーと緯度経度をパラメータとして設定
        params = {
            "appid": os.environ["CLIENT_ID"],
            "lat": "33.67187",
            "lon": "130.441383",
            "output": "json"
        }

        # APIにリクエストを送信
        response = requests.get(url, params=params)

        # レスポンスをJSON形式で取得
        data = response.json()

        # JSONファイルとして保存
        with open('json/reverse_geocoder.json', 'w') as f:
            json.dump(data, f)

        # 住所情報を取得
        address = data["Feature"][0]["Property"]["Address"]

        print(address)

    def text_search_spot(self):
        # APIのエンドポイントURL
        url = 'https://places.googleapis.com/v1/places:searchText'

        # リクエストボディ
        payload = {
            'textQuery': '福岡県福岡市西区西都の休憩場所',
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


# TextSearchSpot().text_search_spot()
