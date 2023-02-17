from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime

app=FastAPI()

class Model(BaseModel):
    title:str
    timestamp:datetime
    description:str | None=None

fake_db ={}

@app.put("/items/{id}")
def update_item(id:str,item:Model):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return json_compatible_item_data
