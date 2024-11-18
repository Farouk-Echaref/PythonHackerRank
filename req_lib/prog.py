#!/usr/bin/python3

import requests
from requests.exceptions import HTTPError

res = requests.get("https://api.github.com")

# check if the req was successful (res < 400 (200 and 399))
if res:
    if res.status_code == 200:
        content = res.content
        json = res.json
        print(json)
elif res.status_code == 404:
    print("Not Found.")
    

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    response = requests.get(url)
    response.raise_for_status()
except 