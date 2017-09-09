import knot

from . import wsgi


def main():
    container = knot.Container()
    wsgi.setup(container)
    return container
