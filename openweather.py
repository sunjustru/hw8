import json
import requests

url = "https://api.weather.yandex.ru/v1/informers?lat=55.75396&lon=37.620393"

querystring = {"lang": "ru_RU", "X-Yandex-API-Key": "8347ae39-8ed9-4104-a981-6184d634d197"}



response = requests.get(url, params=querystring)

print(response.json())
