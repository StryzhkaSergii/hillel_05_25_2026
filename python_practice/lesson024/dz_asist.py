import requests


token = requests.post("http://127.0.0.1:8080/auth",auth=requests.auth.HTTPBasicAuth(username="test_user", password="test_pass"))

print(token.json())