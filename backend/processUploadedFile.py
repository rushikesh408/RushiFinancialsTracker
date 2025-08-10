from fastapi import FastAPI, UploadFile, HTTPException, File
import os
import extract_data
import logging
import image_analyzer
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


def read():
    return {"message": "Hello, World!"}
 
def process_uploaded_file(file: UploadFile):
    try:
        contents = file.file.read()
        logger.debug(f"File MIME Type: {file.content_type}")
        if file.content_type == 'image/jpeg':
            logger.debug(f"file type here is : {file.content_type}")
            logger.debug(f"File name: {file.filename} ")
            with open(file.filename, 'wb') as f:
                logger.debug(f"Writing file: {file.filename}")
                f.write(contents)
                uploadedFilePath = os.path.abspath(file.filename)
                image_analyzer.encode_image(uploadedFilePath)
                
        else:
            logger.error(f"Unsupported file type: {file.content_type}")
            raise HTTPException(status_code=400, detail="Unsupported file type")
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}