import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class SearchSpot:
    def __init__(self) -> None:
        self.place_id = ''

    def reverse_geocoder(self, lat, lon):
        url = "https://map.yahooapis.jp/geocode/V1/geoCoder"
        params = {
            "appid": os.environ["CLIENT_ID"],
            "lat": lat,
            "lon": lon,
            "output": "json"
        }
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code != 200 or 'Feature' not in data:
            raise Exception('Failed to get address')
        address = data["Feature"][0]["Property"]["Address"]
        print(address)

    # 案内文とplace_idを返却
    def search_spot(self, lat, lon):
        url = "https://places.googleapis.com/v1/places:searchNearby"

        payload = {
            "includedTypes": ["convenience_store"],
            "maxResultCount": 1,
            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude": lat,
                        "longitude": lon
                    },
                    "radius": 500.0
                }
            },
            "rankPreference": "DISTANCE",
        }

        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': os.environ["GOOGLE_API_KEY"],
            'X-Goog-FieldMask': 'places.displayName,places.formattedAddress,places.priceLevel',
            'Accept-Language': 'ja'
        }

        response = requests.post(url, headers=headers,
                                 data=json.dumps(payload))
        data = response.json()
        if response.status_code != 200 or 'places' not in data:
            raise Exception('Failed to get places')
        places = data['places']
        texts = [place['displayName']['text'] for place in places]

        spot_result = {
            'introduce': """ドライバーが眠くなっています。近くの休憩場所は{}です。紹介してあげてください。""".format(
                texts[0]),
            'place_id': self.get_placeid(texts[0])
        }

        return spot_result

    # placeid取得
    def get_placeid(self, name):
        url = 'https://places.googleapis.com/v1/places:searchText'
        payload = {
            "textQuery": name
        }
        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': os.environ["GOOGLE_API_KEY"],
            'X-Goog-FieldMask': 'places.id,places.displayName,places.formattedAddress'
        }
        response = requests.post(url, headers=headers,
                                 data=json.dumps(payload))
        data = response.json()
        if response.status_code != 200 or 'places' not in data:
            raise Exception('Failed to get place id')
        return data['places'][0]['id']


# SearchSpot().search_spot(33.576924, 130.260898)
