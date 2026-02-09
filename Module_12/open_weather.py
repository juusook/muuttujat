import json
import requests

avain = "7ec1a8950498d1ef3998510266e785d4"
search = input("Enter municipality name: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={search}&appid={avain}&units=metric&lang=fi"

try:
    vastaus = requests.get(request)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        sää_tuloste = json_vastaus["weather"][0]["description"]
        lämpötila = json_vastaus["main"]["temp"]
        print(f"Weather: {sää_tuloste}, Temperature: {lämpötila} Celsius")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")