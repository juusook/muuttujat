import json
import requests

search = input("Enter municipality name: ")

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")