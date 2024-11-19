#!/usr/bin/python3

import requests
from requests.exceptions import HTTPError

res = requests.get("https://api.github.com")

# check if the req was successful (res < 400 (200 and 399))
if res:
    if res.status_code == 200:
        content : bytes = res.content
        json = res.json
        print(json)
elif res.status_code == 403:
    print("Rate limit")
elif res.status_code == 404:
    print("Not Found.")
    

URLS = ["https://api.github.com", "https://realpython.com/python-requests/", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        # info about metadata for ex: HEADERS
        headers = response.headers
        # print(headers)
        # dict lookup (case insensitive) : headers["content-type"]
        print(headers["Content-Type"])
        # output: 'application/json; charset=utf-8'
        paylod_bytes : bytes = response.content
        # enforce encoding
        # response.encoding = "utf-8"
        paylod_str : str = response.text
        print("----------------- Serialized JSON:")
        print(paylod_str)
        print()
        # can use json.loads() to deserialize it
        print("----------------- Dictionary format: (Deserialized)")
        payload_dict = response.json()
        print(payload_dict)
        
        # can access values like with key/val:
        emo_url : str = payload_dict["emojis_url"]
        # output from the payload: 'https://api.github.com/emojis'
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"Other error occured: {err}")
    else:
        print("Success.")
    break