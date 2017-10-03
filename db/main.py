from pymongo import MongoClient


def mongo_connection(container):
    return MongoClient()


def main_mongo_db(container):
    return container('db.main.mongo_connection')['main']
