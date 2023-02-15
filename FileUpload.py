from fastapi import FastAPI,File,UploadFile

app = FastAPI()

@app.post('/upload')
def postFile(file:bytes = File()):
    return {
        "fileDetails":len(file)
    }

@app.post('/uploadFile/')
async def create_upload_file(file:UploadFile):
    return {
        "filename":file.filename,
        "filetype":file.content_type,
        "max_size":file.spool_max_size,
  }