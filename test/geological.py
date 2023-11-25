import requests

geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
data = requests.get(geo_request_url).json()
print("緯度:", data['latitude'])
print("経度:", data['longitude'])
