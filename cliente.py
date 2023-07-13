import requests
response = requests.get("http//localhost:8000/data/key1")
print(response.json())

response = requests.put("http//localhost:8000/data/key1",data={"value": "updated_value2"}) 
                       