from fastapi import FastAPI,status
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    instagram_id:str
    college:str

@app.get('/',status_code=status.HTTP_200_OK)
def getUser():
    return {
        "hello":"kitty"
    }

@app.post('/user/',status_code=status.HTTP_201_CREATED)
def getUser(user:User):
    if not user:
        return {
            "message":"no data given",
            "status_code":status.HTTP_400_BAD_REQUEST,
            "data":User,
            "created_at":datetime.now()
        }
    return {
        "hello":"everyone"
    }