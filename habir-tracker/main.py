from http.client import responses
from datetime import datetime
import requests

USERNAME = 'hyoseong'
TOKEN = 'ganplankforeverrrrr'
GRAPH_ID = 'ganplank'
pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.now()
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response.text)

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


postit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
postit_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

# response = requests.post(url=postit_endpoint, json=postit_params, headers= headers)
# print(response.text)

update_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params = {
    'quantity': '5',
    'optionalData': today.strftime('%Y%m%d')
}

response = requests.put(url=update_endpoint, json=update_params, headers= headers)
print(response.text)
