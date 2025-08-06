from fastapi import FastAPI, UploadFile, HTTPException, File
import extract_data
import logging
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
            with open(file.filename, 'rb') as f:
                logger.debug(f"Writing file: {file.filename}")
                #f.write(contents)
                extract_data.extract_data(file.filename)
        else:
            logger.error(f"Unsupported file type: {file.content_type}")
            raise HTTPException(status_code=400, detail="Unsupported file type")
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}