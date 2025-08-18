from fastapi import FastAPI
import os
import Database.mongo_db as mongo_db
from bson.json_util import dumps

import json

total_exp = {
    
}


def list_merchants():
    expenses_list = []
    mongo_db.get_database()
    print("Fetching merchants from the database")
    merchant_collection =  mongo_db.get_collection().find()

    list_merchants = list(merchant_collection)
    print(f'length of list= {len(list_merchants)}')
    json_merchants = dumps(list_merchants)

    bill = json.loads(json_merchants)
    print(f'length of bill= {len(bill)}')

    for r in range(0, len(bill)):
        bill = json.loads(json_merchants)[r].get('json_output')
        merchant_name = json.loads(bill).get('merchant_name')
        total_exp[merchant_name] =  total_exp.get(merchant_name,0.0)+  json.loads(bill).get('total_cost')

    return total_exp

   
   
