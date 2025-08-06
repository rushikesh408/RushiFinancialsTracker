from openai import OpenAI
from fastapi import FastAPI, UploadFile, HTTPException, File
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()
# Initialize OpenAI client with API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

def extract_data(file):
    print("inside extract_data function")
    try:
         client = OpenAI(api_key=openai_api_key)     
         resp = client.files.create(
            file=open(file, "rb"),
            purpose="vision"
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        
    
    print(f"File ID: {resp.id}")
    content = client.files.content(resp.id)
    print(content)
