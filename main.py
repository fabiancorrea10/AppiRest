from fastapi import FastAPI
import json 
#json_data = '{("author": "Chinua Achebe", "language":"English" , "title": "Things Fall Apart"), ( "author": "Hans Christian Andersen","language": "Danish", "title": "Fairy tales")}'
data = {}
with open("books.json") as j:
    data = json.load(j)
          
app = FastAPI()
@app.get("/data/[num]")
async def ingresar_nro(num: int):
    if num>=0 and num<100:
        print(f"titulo",data[num]["title"])
        print(f"idioma",data[num]["language"])
        print(f"autor",data[num]["author"])
        
    else:
        print ("El nro ingresado no es correcto, adios")
        exit
        
@app.put("/lenguaje/[num]{value}")
async def lenguaje(num: int, valor: str):
    if num>=0 and num<100:
        data[num]["language"] = valor
        return {"message": "Data updated successfully"}
    else:
        return {"message": "Key not found"}  