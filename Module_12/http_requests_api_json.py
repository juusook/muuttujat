import requests
import json

hakusana = "xfiles"

url = "https://api.tvmaze.com/search/shows?q=" + hakusana



response = requests.get(url)

json_data = response.json()

print(json_data)
#ensimmäinen alkio json datasta eli sanakirja
print(json_data[0])
print(json_data[0]['show'])
print(json_data[0]['show']['name'])
print(json_data[0]['show']['genres'][2])

print(json.dumps(json_data, indent=2))