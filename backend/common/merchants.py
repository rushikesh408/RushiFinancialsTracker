from fastapi import FastAPI
import os
import Database.mongo_db as mongo_db
from bson.json_util import dumps

import json

def list_merchants():
    mongo_db.get_database()
    print("Fetching merchants from the database")
    merchant_collection =  mongo_db.get_collection().find()
    list_merchants = list(merchant_collection)
    json_merchants = dumps(list_merchants)
    
    for json_merchant in json_merchants:
        print(json_merchant)
        #merchantsjsonoutput = json.loads(json_merchant).get("json_output")
        #print(json.loads(merchantsjsonoutput).get("merchant_name")) 
 
        
            
    return True
   
