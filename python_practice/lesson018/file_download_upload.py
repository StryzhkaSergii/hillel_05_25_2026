import requests

url = "https://www.google.com/tia/tia.png"
response = requests.get(url)

with open("some_image.png", "wb") as f:
    f.write(response.content)

with open("some_image.png", "rb") as f:
    data = {"file_name": f.read()}

upload_response =  requests.post(url, files=data)
pass