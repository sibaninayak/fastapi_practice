from fastapi import FastAPI , Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "token")

class User(BaseModel):
    username:str
    email:str | None=None
    full_name:str |None = None
    disabled :bool |None = None


def fake_decode_token(token):
    return User(
        username=token + "fakecoded", email="kitty@gmail.com" , full_name="sibani nayak"
    )

@app.get('/')
def getData(token:str = Depends(oauth2_scheme) ):
    return {
        "token": token
    }