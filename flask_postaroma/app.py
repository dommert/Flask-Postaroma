# Flask-Postaroma
# version 1.0-alpha
# (C) Abstergo 2020

## app.py

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# Import Config
app.config.from_pyfile('config.cfg')

# Load Routes
from flask_postaroma.routes import *



if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'],
            port=app.config['SERVER_PORT'],
            debug=app.config['DEBUG'])
