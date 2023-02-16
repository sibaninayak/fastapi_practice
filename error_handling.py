from fastapi import FastAPI,HTTPException,status,Request
import base64
from fastapi.responses import JSONResponse

app = FastAPI()

class CustomError(Exception):
    def __init__(self,name:str)->None:
        self.name=name

@app.exception_handler(CustomError)
async def error_handler(request:Request, exc:CustomError):
    return JSONResponse(
        status_code=400,
        content={
        "message":f"Opps! {exc.name}did something..."
        }
    )

@app.exception_handler(CustomError)
async def error_handler(request:Request, exc:CustomError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
        "message":f"Opps! {exc.name}is unauthorized..."
        }
    )


@app.post('/user/{username}')
def getUser(username:str):
    if username != 'kitty':
        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail="username is invalid",
                            headers={"name":"sibani nayak"}
                            )
    return {
        "user":username
    }

@app.post('/user/{username}/{token}')
def getUser(username:str , token:str):
    if token != 'token data':
        raise CustomError(name=token)
    if username != 'kitty':
        raise CustomError(name=username)
    return {
        "user":username,
        "token": token
    }