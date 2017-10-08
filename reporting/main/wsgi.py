import falcon
from falcon_auth import FalconAuthMiddleware, TokenAuthBackend

from reporting.db.gateway import get_user_by_auth_token
from reporting.web.images import ContextImageResource


def setup(container):
    container.add_service(app, name='web.wsgi.app')
    container.add_service(resource, name='web.images.resource')
    setup_routing(container)


def app(container):
    return falcon.API(middleware=[auth_middleware()])


def resource(container):
    return ContextImageResource()


def auth_middleware():
    auth_backend = TokenAuthBackend(get_user_by_auth_token)
    auth_middleware = FalconAuthMiddleware(auth_backend)
    return auth_middleware


def setup_routing(container):
    container('web.wsgi.app').add_route(
        '/image',
        container('web.images.resource'),
    )
