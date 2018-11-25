# Setup File

from setuptools import setup

setup(
    name='flask-netpad',
    packages=['flask'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-mongoengine',
    ],
)
