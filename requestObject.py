from fastapi import FastAPI,Request

app = FastAPI()

@app.get('/')
def showBody(req:Request):
    return{
        "baseurl":req.base_url,
        "method":req.method,
        "host":req.headers
    }