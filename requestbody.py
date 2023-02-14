from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class family(BaseModel):
    name:str
    father_name:str
    mother_name:str
    brother_name: str
    
    
@app.get('/user')
def bio(user:family):
    return {
        "message":"user created succesfull",
        "status_code":201,
        "data":user,
    }
  


