import falcon

from reporting.web.images.context import ContextImageResource
from reporting.web.images.details import DetailsImageResource
from reporting.web.report import ReportResource


def setup(container):
    container.add_service(app, name='web.wsgi.app')
    container.add_service(
        context_image_resource,
        name='web.images.context_resource',
    )
    container.add_service(
        details_image_resource,
        name='web.images.details_resource',
    )
    container.add_service(
        report_resource,
        name='web.report.resource'
    )
    setup_routing(container)


def app(container):
    return falcon.API()


def context_image_resource(container):
    return ContextImageResource()


def details_image_resource(container):
    return DetailsImageResource()


def report_resource(container):
    return ReportResource()


def setup_routing(container):
    container('web.wsgi.app').add_route(
        '/image/context',
        container('web.images.context_resource'),
    )
    container('web.wsgi.app').add_route(
        '/image/details',
        container('web.images.details_resource'),
    )
    container('web.wsgi.app').add_route(
        '/report',
        container('web.report.resource'),
    )
