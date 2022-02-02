import requests


def params(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    points = [list(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())),
              list(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split()))]
    toponym_size = [str(points[1][0] - points[0][0]), str(points[1][1] - points[0][1])]
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(toponym_size),
        "l": "map",
        "pt": f"{float(toponym_longitude)},{float(toponym_lattitude)},flag"
    }
    return map_params
