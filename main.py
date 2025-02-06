import json
import requests

from geopy.distance import distance
import folium

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


# with open("coffee.json", "r", encoding="CP1251") as coffee:
#     file_contents = coffee.read()
# coffeeshops = json.loads(file_contents)
# # first_coffee = coffeeshops[0]
# list_coffeshops = []
# question = input("Где вы находитесь?: ")
# coords = fetch_coordinates(apikey, "Красная площадь")
# print(coords)
# print(question)
# for our_coffee in coffeeshops:
#     name_first_coffee = our_coffee["Name"]
#     coordinates = our_coffee["geoData"]["coordinates"]
#     dist = distance(coords[::-1], coordinates[::-1]).km
#     print("Ваши координаты", coordinates)
#     # pprint(our_coffee)

#     caffee = {"name": name_first_coffee, "distance": dist, "coord": coordinates}

#     list_coffeshops.append(caffee)
# pprint(list_coffeshops)
# print("Расстояние : ", distance(coords, coordinates), "km")


with open("coffee.json", "r", encoding="CP1251") as coffee:
    file_contents = coffee.read()
coffeeshops = json.loads(file_contents)
# coffeeshops_d = coffeeshops[0:5]
list_coffeshops = []
question = input("Где вы находитесь?: ")
coords = fetch_coordinates(apikey, question)
nearest_coffee = min(
    coffeeshops,
    key=lambda coffee: distance(
        coords[::-1], coffee["geoData"]["coordinates"][::-1]
    ).km,
)


min_distance = distance(coords[::-1], nearest_coffee["geoData"]["coordinates"][::-1]).km
print(coords)
print("distance: ", min_distance)
pprint(nearest_coffee["Name"])
pprint(nearest_coffee["Longitude_WGS84"])
pprint(nearest_coffee["Latitude_WGS84"])
pprint(coffeeshops)
