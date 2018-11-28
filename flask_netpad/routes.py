# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## routes.py


from flask import request, jsonify
from flask_netpad.app import app
from flask_netpad.netpad import *


@app.route('/')
def index():
    return 'Hello World!'

# Sample
@app.route('/about')
def about_route():
    if request.args.get('var') is None:
        testVar = 'Unknown'
    else:
        testVar = request.args.get('var')
    data = 'About Me '+testVar
    return data



# -- Notes Routes --

# List Note
@app.route('/note/')
def listNote_route():
    lim = request.args.get('limit')
    if isinstance(lim, str) == True:
        lim = 5
    note = listNote().limit(lim)
    return jsonify(note)

# Read Note
@app.route('/note/<nid>/')
def readNote_route(nid):
    note = readNote(id=nid).first()
    #note = Note.objects(slug=nid).first()
    return jsonify(note)

# View Note





# >>> CATCH ALL <<<
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You wanted path: %s' % path

