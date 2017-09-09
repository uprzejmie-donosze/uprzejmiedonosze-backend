import falcon

from reporting.web.images import ContextImageResource


def setup(container):
    container.add_service(app, name='web.wsgi.app')
    container.add_service(resource, name='web.images.resource')
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
