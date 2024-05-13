from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://romalearn:S13o1ebSZ63pTcsV@prominb0.3pd0e3e.mongodb.net/?retryWrites=true&w=majority")
    db = client.pyweb9hw
    return db
