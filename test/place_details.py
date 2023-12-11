import requests
import os
import webbrowser

from dotenv import load_dotenv

load_dotenv()


# ヘッダー情報
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': os.environ["GOOGLE_API_KEY"],  # あなたのGoogle APIキー
    'X-Goog-FieldMask': 'googleMapsUri'  # websiteを取得するために指定
}

# GETリクエストを実行
response = requests.get('https://places.googleapis.com/v1/places/ChIJZx4pw5jrQTURaTr3uAUhpX4',
                        headers=headers)

# レスポンスのJSONを取得
data = response.json()
# GoogleマップのURLを取得
google_maps_url = data['googleMapsUri']
# print(google_maps_url)
webbrowser.open(google_maps_url)
