from fastapi import FastAPI, UploadFile, HTTPException, File
from processUploadedFile import process_uploaded_file, read
import logging
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

#from processUploadedFile import process_upload_file

app = FastAPI()
@app.get("/")
def read():
    return read()




@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return process_uploaded_file(file)
