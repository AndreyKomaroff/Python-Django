import requests
import json

url = "https://vk.com/kamarooff"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print("Error occurred while fetching data")