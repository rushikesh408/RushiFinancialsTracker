from fastapi import FastAPI, UploadFile, HTTPException, File
from processUploadedFile import process_uploaded_file, read
import logging
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

#from processUploadedFile import process_upload_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)
 
@app.get("/")
def read():
    return read()

 


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return process_uploaded_file(file)
