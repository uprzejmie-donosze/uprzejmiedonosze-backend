from setuptools import setup

setup(
    name='Uprzejmie donosze',
    version='0.1',
    description='App for reporting car related events',
    author='Piotr Kopalko',
    author_email='copalco@gmail.com',
    packages=['reporting'],
    install_requires=[
        'falcon==1.2.0',
        'knot==0.4.0',
    ],
    extras_require={
        'test': (
            'pytest==3.1.3',
            'mypy==0.521',
        ),
    },
)
