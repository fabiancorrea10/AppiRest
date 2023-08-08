import requests
url = 'http://192.168.84.110:8000'
response = requests.get(url)
print(response.status_code)
print(response.json())

response = requests.put(url) 
                        