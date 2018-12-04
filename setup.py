# Setup File

from setuptools import setup

setup(
    name='Flask-Postaroma',
    packages=['flask'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-mongoengine',
    ],
)
