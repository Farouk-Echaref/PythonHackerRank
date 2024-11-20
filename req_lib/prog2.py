#!/usr/bin/python3

import requests
from requests.exceptions import HTTPError

# Query Strings

response = requests.get("https://api.github.com/search/repositories",
                        params={"q": "language:python", "sort": "stars", "order": "desc"},
                        )
# or in bytes
# res = requests.get("https://api.github.com/search/repositories",
#                    params=b"q=language:python?sort=stars?order=desc",
#                    )

repo_payload = response.json()

# list contains multiple dicts, each dict contains data about a repo
popular_repos = repo_payload["items"]
print()
print()
print()
# slice to only get the first first 3 elems
for repo in popular_repos[:3]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"URL: {repo['html_url']}")
    print()
    
# Request headers:

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": '"real python"'},
    headers={"Accept": "application/vnd.github.text-match+json"},
)