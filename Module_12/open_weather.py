import json
import requests

avain = "7ec1a8950498d1ef3998510266e785d4"

search = input("Enter municipality name: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={search}&appid={avain}"
vastaus = requests.get(request)
json_vastaus = vastaus.json()
print(json.dumps(json_vastaus, indent=2))

'''try:
    vastaus = requests.get(search)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus[])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")'''