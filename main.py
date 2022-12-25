import requests


USERNAME = "anjel"
TOKEN = "uy9HKg6oJ8g7Hdsjhs"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_ENDPOINT_CREATE = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXELA_ENDPOINT_UPDATE = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20221127"
PIXELA_ENDPOINT_DELETE = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20221127"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit":"minutes",
    "type": "float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}


# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)


# response = requests.post(url=PIXELA_ENDPOINT_GRAPH,json=graph_parameters, headers=headers )
# print(response.text)

pixela_parameters = {
    "date":"20221128",
    "quantity": "60.5",

}

# response = requests.post ( url=PIXELA_ENDPOINT_CREATE, json=pixela_parameters,headers=headers)
# print(response.text)

update_parameters = {
    "quantity": "55",
}

# response = requests.post(url=PIXELA_ENDPOINT_UPDATE, json=update_parameters, headers=headers)
# print(response.text)


response = requests.post(url=PIXELA_ENDPOINT_DELETE, headers=headers)
print(response.text)

