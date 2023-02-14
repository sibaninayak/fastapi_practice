from fastapi import FastAPI,Cookie

app = FastAPI()

@app.get('/cooki')
def home(name:str|None = Cookie(default=None)):
    return {
        "home":name
    }