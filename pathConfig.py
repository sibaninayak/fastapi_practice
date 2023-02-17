from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Tags(Enum):
    KITTY = 'kitty',
    LUCKY = 'lucky'

class item(BaseModel):
    name:str
    description:str

@app.get('/user/',tags=['kitty'],summary='part1')
def getuser():
    return {
        "hello":"kitty"
    }
 
@app.get('/user1/',tags=[Tags.KITTY],description='im a good girl')
def getuser1():
    return {
        "hello":"kitty"
    }
 
@app.get('/user2/',tags=[Tags.LUCKY],deprecated=True)
def getuser2():
    return {
        "hello":"kitty"
    }
 
@app.get('/user3/',tags=['kitty'])
def getuser( Item:item):
    """
    Create an item with all the information:

    -"name":each item must have a name,
    -"description":a long description
    """
    return {
        Item
    }

@app.get('/user3/',tags=['kitty'],response_model=item,response_description="the created item")
def getuser( Item:item):
    """
    Create an item with all the information:

    -"name":each item must have a name,
    -"description":a long description
    """
    return Item
    
  