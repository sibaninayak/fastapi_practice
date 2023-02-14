from fastapi import FastAPI,Body
from pydantic import BaseModel,Field,Required

app = FastAPI()


class biodata(BaseModel):
    username:str|None = Field(default=Required,max_length=5)
    age:int
    education:str|None = Field(default="B.TECH",max_length=20,min_length=10)
    college:str|None = Field(default="Roland institute of technology")
    hobbby:str|None = Field(default="watching kdrama and bts")
    father_name:str
    mother_name:str
    brother_name:str
    dream:str|None = Field(default="Southkorea")
    
@app.post('/data')
def Data(bio:biodata=Body(embed=True)):
    return {
        "bio":biodata
    }    

class Item(BaseModel):
    username:str|None = Field(default=Required,max_length=5)
    age:int

@app.put('/items')
def update_item(
       item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "kitty",
                    "description": "A very nice girl",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "lucky",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "sibani",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
         
    results={"item": item}
    return results
    
    
    
    


