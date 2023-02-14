from fastapi import FastAPI,Path,Query,Request
from pydantic import Required

app = FastAPI()

#simple path param
@app.get('/{path}')
def pathparam(path):
    print({"path":path})
    return {
        "path":path
    }

#simple path param with class
@app.get('/path/{path}')
def pathparamswithpath(path:str | None = Path(default = Required , description ="heloo kitty",deprecated=True,include_in_schema=True)):

    print({"path":path})
    return {
        "path":path
    }

#simple path param with path class and query params with query class
@app.get('/path/query/{path}')
def pathandQueryParam(
       q: str |None = Query(default=Required,description="hello sibani"),
       path:int|None = Path(default=None , description="hello kitty",ge=2,le=5,deprecated=True,include_in_schema=True)):
   print({"path":path})
   if q:
       return{
           "query":q,
           "path":path
        }
    
#simple path param with path class and query param with query class
@app.get('/req/{path}')
def requestObj(
      req :Request,
      q :str|None = Query(default=Required , description="bangtan boys"),
      path:int | None = Path(default=None , description= "BTS", ge=2,le=5, deprecated=True,include_in_schema=True )):
    print({"path":path})
    if q:
        return {
            #"query":q,
            "path":path,
            "query1":req._query_params
        }
