from fastapi import FastAPI, UploadFile, HTTPException, File
from processUploadedFile import process_uploaded_file, read
from common.merchants import list_merchants
from common.totals import readTotals
from common.find_merchant_totals import readMerchantTotals
import os
import logging
from typing import Optional
from fastapi import Query
from common.filtered_by_date import fetch_by_dates

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

# from processUploadedFile import process_upload_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return process_uploaded_file(file)


@app.get("/merchants")
def list_merchant():
    return list_merchants()


@app.get("/totals")
def get_totals():
    return readTotals()


@app.get("/merchant_totals")
def get_merchant_totals(
    q: Optional[str] = Query(
        None, description="Type part of a merchant name (e.g. 'tar' for TARGET)"
    ),
    limit: int = 10,
):
    # If q is None -> ALL merchants; if q has text -> filter & limit
    return readMerchantTotals(query=q, limit=limit)


@app.get("/filtered_by_date")  # (typo fixed from /filterd_by_date)
def get_filtered_by_date(
    start_date: str = Query(..., description="YYYY-MM-DD"),
    end_date: str = Query(..., description="YYYY-MM-DD"),
):
    fetch_by_dates(start_date, end_date)
