import requests
response = requests.get("http//192.168.0.19:8000/data/num")
print(response.json())

response = requests.put("http//192.168.0.19:8000/data/num",data={"value": "updated_value2"}) 
                        