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
        return{f"titulo":data[num]["title"],"idioma":data[num]["language"],"autor":data[num]["author"]}
        
        
        
    else:
        return{"El nro ingresado no es correcto, adios"}
        exit
        
@app.put("/lenguaje/[num]{value}")
async def lenguaje(num: int, valor: str):
    if num>=0 and num<100:
        data[num]["language"] = valor
        with open("books.json",'w') as f:
            json.dump(data,f,indent=4)
        return {"mensaje": "actualizacion exitosa"}
    else:
        return {"mensaje": "info no actualizada"}  