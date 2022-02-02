import sys
from io import BytesIO
import requests
from PIL import Image

import find


map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = find.params(" ".join(sys.argv[1:]))
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
