from fastapi import FastAPI , Response
from fastapi.responses import RedirectResponse , JSONResponse
from pydantic import BaseModel

app = FastAPI()

class BTS(BaseModel):
    description:str
    member1:str
    member2:str
    member3:str
    member4:str
    member5:str
    member6:str
    member7:str

@app.get('/')
def bangtan(BTS:str):
    return {
        "bts":BTS

    }
# @app.get('/')
# def Bangtan():
#     return [
#         BTS(member6="taehyung"),
#         BTS(member6="jungkook"),

#     ]

# @app.post('/',response_model=list[BTS])
# def Bangtan():
#     return [
#         BTS(member6="taehyung"),
#         BTS(member7="jeon jungkook")
#     ]

@app.get('/portal')
async def get_portal(teleport:bool =  False) -> Response:
    if teleport:
        return RedirectResponse(url="https://youtu.be/51SwozTN9qM")
    return JSONResponse(content={"message":"here's your interdimentional portal","status_code":200})