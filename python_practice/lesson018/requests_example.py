import requests
#pip install requests

response = requests.get(url= "https://swapi.info/api/people/1")

status_code = response.status_code
text = response.text
headers = dict(response.headers)

response_json = response.json() #json.loads(response.text)

print("status code", status_code)
print("headers", headers)
print("text", text)
print("-"*80)
print("json", response_json)

print(response_json.get("name"))

print(type(text))
print(type(response_json))