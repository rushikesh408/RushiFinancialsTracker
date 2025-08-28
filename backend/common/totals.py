from fastapi import FastAPI
import Database.mongo_db as mongo_db
import json
from bson.json_util import dumps


def readTotals():
    totalExpense = {"Total Expenses": 0.0}
    total = 0.0
    merchant_collection = (
        mongo_db.get_collection().find()
    )  # Implement the logic to read totals from the database
    list_merchants = list(merchant_collection)
    print(f"length of list= {len(list_merchants)}")
    json_merchants = dumps(list_merchants)
    print(f"json_merchants= {json_merchants}")
    bill = json.loads(json_merchants)

    for r in range(0, len(bill)):
        bill = json.loads(json_merchants)[r].get("json_output")
        merchant_name = json.loads(bill).get("merchant_name")
        # total = float(json.loads(bill).get("total_cost")) + total
        total += float(json.loads(bill).get("total_cost"))
        totalExpense["Total Expenses"] = total

    return totalExpense
