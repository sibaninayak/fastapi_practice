import time
from fastapi import FastAPI,Request

app = FastAPI()

@app.middleware('http')
async def callMiddleWare(req : Request , nextfn):
    start_time = time.time()
    response = await nextfn(req)
    process_time = time.time()-start_time
    response.headers["X-process-Siri's Time"] = str(process_time)
    #response.headers['about myself'] = str('kitty')
    return response


@app.get('/')
async def getData():
    time_taken = time.gmtime(1677110400)
    print(time_taken)
    return {
           "createdAt":f'{time_taken.tm_mday}-{time_taken.tm_mon}-{time_taken.tm_year}'
    }

