from fastapi import FastAPI

app = FastAPI()
products_name:list = [{"item_name":"army bomb" }, {"item_name" : "bts photocards"}, {"item_name":"yet to come album"}]

@app.get("/users")
def username():
    return {
        "name": "kitty",
        "age":20
    }

#query params
@app.get("/products/")
def amazon(skip: int = 0 , limit: int = 10):
    return products_name[skip:skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id:str,q:str):
    if q:
        return {"item_id": item_id,"q":q}
    return {"item_id" :item_id}