import knot

from reporting.main import wsgi


def main():
    container = knot.Container()
    wsgi.setup(container)
    return container


def create_app(env, start_response):
    container = main()
    return container('web.wsgi.app')(env, start_response)
