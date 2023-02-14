from fastapi import FastAPI,Query

app = FastAPI()

@app.get('/kitty/')
def query(village:str ):
    results = {"data": [{"name":"sibani nayak"},{"age":20}]}
    if village:
        results.update({"village":village})
    return results

@app.get('/sibani/')
def query_validation(btsmembers: str | None = Query(default=None, max_length=20)):
    results = {"data": [{"member1": 'taehyung'}, {" member2": "jungkook"}]}
    if btsmembers:
        results.update({"fav": btsmembers})
    return results

@app.get('/lucky/')
def query_validation(btsmembers: str | None = Query(default=None, max_length=20 , min_length=10)):
    results = {"data": [{"member1": 'taehyung'},
                        {" member2": "jungkook"}]}
    if btsmembers:
        results.update({"fav": btsmembers})
    return results


#multiple query parameter
@app.get("/jk/")
def btsmembers(members:list[str] = None):
    return {
        "members":members
    }


@app.get("/v/")
def btsmembers(members:list[str] = Query(default=["v","jk"])):
    return {
        "members":members
    }

@app.get('/fav/')
def btsmembers(members:list[str] =
Query(default=None,
description="saranghae",
title="BTS",
deprecated=True,
alias="Annyeonghaseyo",
include_in_schema=True
)):
    return {
        "members" : members
    }
