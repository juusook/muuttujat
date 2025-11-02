import json
import requests


pyyntö = "https://api.chucknorris.io/jokes/random"
'''vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()
print(json.dumps(json_vastaus, indent=2))'''


try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")