import requests

url = "http://127.0.0.1:5000/admins/create"
data = {"username": "admin1", "email": "admin1@example.com", "password": "12345"}
response = requests.post(url, json=data)

print(response.status_code)
