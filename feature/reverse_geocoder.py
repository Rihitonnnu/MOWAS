import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

# Yahoo!リバースジオコーダAPIのURL
url = "https://map.yahooapis.jp/geocode/V1/geoCoder"

# いずれは関数として使ってあげたい

# APIキーと緯度経度をパラメータとして設定
params = {
    "appid": os.environ["CLIENT_ID"],
    "lat": "33.57753926992066",
    "lon": "130.26094105389342",
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
