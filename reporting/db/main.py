import knot
from pymongo import MongoClient


USERS = 'users_collection'


def mongo_connection(container):
    return MongoClient()


def main_mongo_db(container):
    return container('reporting.db.main.mongo_connection')['main']


def users_collection(container):
    return container('reporting.db.main.main_mongo_db').users


def configure_db_connection():
    container = knot.Container()
    container.add_service(mongo_connection, name='reporting.db.main.mongo_connection')
    container.add_service(main_mongo_db, name='reporting.db.main.main_mongo_db')
    container.add_service(users_collection, name=USERS)
    return container


db = configure_db_connection()
