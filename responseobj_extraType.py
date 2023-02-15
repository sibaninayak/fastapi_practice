from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    passward:str
    email:EmailStr
    full_name:str|None=None

class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_name:str|None=None

class UserInDB(BaseModel):
    username:str
    hashed_passward:str
    email:EmailStr
    full_name:str|None=None

def fake_passward_hasher(raw_passward:str):
    return "supersecret"+ raw_passward

def fake_save_user(user_in:UserIn):
    hashed_passward = fake_passward_hasher(user_in.passward)
    user_in_db = UserInDB(**user_in.dict(),hashed_passward=hashed_passward)
    print("user saved!..not really")
    return user_in_db

@app.post('/user')
def createUser(user:UserIn):
    user_saved= fake_save_user(user)


# @app.get('/')
# def getdata():
#     return {
#         "hello":"kitty"
#     }