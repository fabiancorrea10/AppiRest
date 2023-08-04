import requests
response = requests.get("http//localhost:8000/data/num")
print(response.json())

response = requests.put("http//localhost:8000/data/num",data={"value": "updated_value2"}) 
                        