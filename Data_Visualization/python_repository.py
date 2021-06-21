#API call from Github for python repository with star

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f"Status code:{r.status_code}")

#store API response in a variable
repsonse_dict = r.json()

#process results
print(repsonse_dict.keys())