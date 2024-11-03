from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://")
    db = client.dbname
    return db
