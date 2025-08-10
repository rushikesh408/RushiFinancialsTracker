
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rushikesh:RUSHIKESH@cluster0.hihrfw3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def get_database():
# Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def get_collection():
    try:
        db = client["RushiFinancials"]
        collection = db["Financials"]
        print("Collection accessed successfully.")
        print(f"Collection name: {collection.name}")
        return collection
    except Exception as e:
        print(f"An error occurred while accessing the collection: {e}")
        return None
    
## write json_output to mongo db
def insert_json_output(json_output):
    collection = get_collection()
    try:
        collection.insert_one({"json_output": json_output})
        print("JSON output inserted into MongoDB successfully.")
    except Exception as e:
        print(f"An error occurred while inserting JSON output: {e}")