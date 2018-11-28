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



# ==== Notes Routes =====

# --- List Note
@app.route('/note/')
def pageNote_route():
    # If page=all return list
    if request.args.get('page') == 'all':
        print('listall')
        note = listNote(deleted=False)
        return jsonify(note)

    if request.args.get('page') is None:
        page = 1
    else:
        page = int(request.args.get('page'))

    if request.args.get('per_page') is None:
        pg_limit = 2
    else:
        pg_limit = int(request.args.get('per_page'))

    note = pageNote(page=page, per_page=pg_limit)
    return jsonify(note)


# --- Read / View Note
@app.route('/note/<nid>/')
def readNote_route(nid):
    #note = readNote(id=nid).first()
    note = readNote(id=nid)
    return jsonify(note)


# --- List All Note
@app.route('/list/note/')
def listNote_route():
    '''
    lim = request.args.get('limit')
    if isinstance(lim, str) != True:
        lim = 5
        print('xx')
    '''

    note = listNote()
    return jsonify(note)


# >>> CATCH ALL <<<
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You wanted path: %s' % path

