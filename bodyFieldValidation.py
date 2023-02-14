from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

app = FastAPI()

@app.get('/')
def getreq():
    return {
        "kitty":"hello kitty"
    }

class BodyField(BaseModel):
    name:str
    description:str |None = Field(
        default=None,description='enter here the description')
    currency:float |None = Field(default=None)

@app.post('/bodydata')
def getBodyData(Profile:BodyField = Body(embed=True)):
    return {
        "body field":Profile
    }