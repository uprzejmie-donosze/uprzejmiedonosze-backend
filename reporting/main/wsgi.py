import falcon

from db.main import main_mongo_db, mongo_connection
from reporting.web.images import ContextImageResource


def setup(container):
    container.add_service(app, name='web.wsgi.app')
    container.add_service(resource, name='web.images.resource')
    container.add_service(mongo_connection, name='db.main.mongo_connection')
    container.add_service(main_mongo_db, name='db.main.main_mongo_db')
    setup_routing(container)


def app(container):
    return falcon.API()


def resource(container):
    return ContextImageResource()


def setup_routing(container):
    container('web.wsgi.app').add_route(
        '/image',
        container('web.images.resource'),
    )
