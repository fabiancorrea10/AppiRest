from fastapi import FastAPI
import json 
#json_data = '{("author": "Chinua Achebe", "language":"English" , "title": "Things Fall Apart"), ( "author": "Hans Christian Andersen","language": "Danish", "title": "Fairy tales")}'
data = {}
with open("books.json") as j:
    data = json.load(j)
print(data[1])
print(data[2]['author'])
#print(data['language'])
#print(data['country'])
#print(data['imageLink'])
#print(data['link'])
app = FastAPI()
@app.get("/data/{key}")
async def read_data(key: str):
    if key in data:
        return {libro: data[key]}
    else:
        return {"message": "Key not found"}
@app.put("/data/{key}")
async def update_data(key: str, value: str):
    if key in data:
        data[key] = value
        return {"message": "Data updated successfully"}
    else:
        return {"message": "Key not found"}  