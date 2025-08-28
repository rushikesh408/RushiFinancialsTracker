from datetime import datetime
import Database.mongo_db as mongo_db
from bson.json_util import dumps

import json


def fetch_by_dates(start_date: str, end_date: str):
    total_exp = {}
    expenses_list = []
    mongo_db.get_database()
    print("Fetching data from the database")

    start_time = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_time = datetime.strptime(end_date, "%Y-%m-%d").date()

    print(f"Start date: {start_time}, End date: {end_time}")

    merchant_collection = mongo_db.get_collection().find()

    list_merchants = list(merchant_collection)
    print(f"length of list= {len(list_merchants)}")
    json_merchants = dumps(list_merchants)

    bill = json.loads(json_merchants)
    print(f"length of bill= {len(bill)}")

    for r in range(0, len(bill)):
        bill = json.loads(json_merchants)[r].get("json_output")
        merchant_name = json.loads(bill).get("merchant_name")
        total_exp[merchant_name] = total_exp.get(merchant_name, 0.0) + float(
            json.loads(bill).get("total_cost")
        )

    return total_exp
