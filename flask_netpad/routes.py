# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## routes.py


from flask import request, jsonify
from flask_netpad.app import app


@app.route('/')
def index():
    return 'Hello World!'
