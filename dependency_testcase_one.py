from fastapi import FastAPI,Depends

app = FastAPI()
products_name:list = [{"item_name":"army bomb" }, {"item_name" : "bts photocards"}, {"item_name":"yet to come album"}]

def depending_fn(skip:int = 0, limit:int = 10):
    return products_name[skip:skip +limit]

class DependingClass:
    def __init__(self, skip:int = 0 , limit:int = 10) :
        self.skip = skip;
        self.limit = limit

# def depending_fn(q:str |None = None ,skip:int = 0, limit:int = 10):
#     return {
#         "q":q,
#         "skip":skip,
#         "limit":limit
#     }

# @app.get('/user/')
# def showUser(skip:int = 0 , limit: int = 10):
#     return products_name[skip:skip + limit]

#query params

# @app.get('/user/')
# def showUser(depends :any = Depends(depending_fn)):
#     return depends

@app.get('/user/')
def showUser(depends: DependingClass = Depends(DependingClass)):
    return products_name[depends.skip: depends.skip + depends.limit]