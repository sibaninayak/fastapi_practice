from fastapi import FastAPI,Header

app=FastAPI()

@app.get('/item')
async def read_item(bangtan:str|None=Header(default=None),taehyung : str |None = Header(default=None)):
    return {
        "fav":bangtan,"v":taehyung
    }