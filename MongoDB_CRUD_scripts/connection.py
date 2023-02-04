from pymongo import MongoClient

DATABASE_URL = 'mongodb://localhost:27017/'
DATABASE_NAME = 'contact_handbook'
COLLECTION_NAME = 'contacts'

def conn():
    client = MongoClient(DATABASE_URL)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    return collection