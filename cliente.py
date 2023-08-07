import requests
response = requests.get("http://127.0.0.1:8000/data/num")
print(response.json())

response = requests.put("http://127.0.0.1:8000/data/num",data={"language": "idioma actualizado"}) 
                        