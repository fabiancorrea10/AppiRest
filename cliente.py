import requests
url = 'http://127.0.0.1:8000'
libro = int(input ('Ingrese un nro entre 0 y 99: '))

cad_libro = str(libro)
#http://127.0.0.1:8000/data/[num]?num=90
req = url+"/data/[num]?num="+cad_libro
response = requests.get(req)
print(response.status_code)
print(response.json())

#http://127.0.0.1:8000/lenguaje/[num]{value}?num=6&valor=noruego
idiom = input ("Ingrese nuevo idioma: ")
req1 = url+"/lenguaje/[num]{value}?num="+cad_libro+"&valor="+idiom
response1 = requests.put(req1) 
print(response1.json())                    