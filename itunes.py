import json
import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

# sys.exit exit the whole program, brek exit from only loop

# term=weezer
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
data = response.json()

for result in data["results"]:
    print(result["trackName"])
