from fastapi import FastAPI , Query,Path,Body
from pydantic import BaseModel

app = FastAPI()

@app.get('/get')
def getMixPath():
    return {
        "message":"hello kitty"
    }

@app.post('/body')
def Postmix(data):
    return {
        "data":data
    }

@app.put('/put/{name}')
def Putmix(*,
           name : str = Path(default=None),
           q:str =Query(default=None),
           b: str):
    return{
        "path": name,
        "q":q,
        "b": b
    }

class BTS(BaseModel):
    member1:str
    member2:str
    member3:str
    member4:str
    member5:str
    member6:str
    member7:str

class Protiviti(BaseModel):
   
    member1:str
    member2:str
    member3:str
    member4:str
    member5:str
    member6:str
    member7:str
    whoisfav:str

@app.post('/bangtan')
def BangtanBoys(whoisyourfav:Protiviti):
    return {
        "data": whoisyourfav
    }


class biodata(BaseModel):
    my_name:str
    father_name:str
    mother_name:str
    brother_name:str


class user(BaseModel):
    username:str
    age:int
    birthday:int
    college:str
    stream:str


# @app.post("/bio/{bio_data}")
# async def update_data(
#     *,
#     bio_data:str,
#     family:biodata,
#     User:user,
#     instagram:str = Body(),
#     q:str
#     ):  

#     results = {"bio_data":bio_data,"family":family,"User":User,"instagram":instagram}
#     if q:
#         results.update({"q":q})
#     return results


@app.put('/bio/{bio_data}')
async def update_user(bio_data:str,user:user=Body(embed=True)):
    results = {"bio_data":bio_data,"user":user}
    return results