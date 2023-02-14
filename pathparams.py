from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def bangtan():
    return {
        "bts member"
    }

@app.get("/members")
def bangtan():
    return {
        "rm":"kim namjoon",
        "jin":"kim seokjin",
        "suga":"min yoongi",
        "jhope":"jung hoseok",
        "jimin":"park jimin",
        "v":"kim taehyung",
        "jk":"jeon jungkook"
    }
       
#path params
@app.get("/members/{name}")
def members(name):
    return {
        "fav member" : name
    }
    
    