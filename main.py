import json
import requests

from geopy import distance

from pprint import pprint


apikey = "6104f5f0-5fed-4b3f-9007-36072e3b49f9"  # ваш ключ


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(
        base_url,
        params={
            "geocode": address,
            "apikey": apikey,
            "format": "json",
        },
    )
    response.raise_for_status()
    found_places = response.json()["response"]["GeoObjectCollection"]["featureMember"]

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant["GeoObject"]["Point"]["pos"].split(" ")
    return lon, lat


with open("coffee.json", "r", encoding="CP1251") as coffee:
    file_contents = coffee.read()
coffeeshops = json.loads(file_contents)
# first_coffee = coffeeshops[0]
for our_coffee in coffeeshops:
    question = input("Где вы находитесь?: ")
    name_first_coffee = our_coffee["Name"]
    coordinates = our_coffee["geoData"]["coordinates"]
    distance = distance.distance(question, our_coffee)
    print("Ваши координаты", coordinates)
    # pprint(our_coffee)

    caffee = {
        "name": name_first_coffee,
        "distance": distance,
        "coord": coordinates,
    }

    coffeeshops.append(caffee)

    print("Расстояние : ", distance.distance(question, our_coffee).km)
