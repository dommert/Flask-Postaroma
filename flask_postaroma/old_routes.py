# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## old_routes.py


from flask import request, jsonify
from flask_postaroma.app import app
from flask_postaroma.posts import *


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
    data = 'About Me ' + testVar
    return data


# ==== Notes Routes =====

# --- List Post
@app.route('/note/')
def pageNote_route():
    # If page=all return list
    if request.args.get('page') == 'all':
        print('listall')
        note = list(deleted=False)
        return jsonify(note)

    if request.args.get('page') is None:
        page = 1
    else:
        page = int(request.args.get('page'))

    if request.args.get('per_page') is None:
        perpage = 2
    else:
        perpage = int(request.args.get('per_page'))

    print(page, perpage)
    note = pagePost(page=page, per_page=perpage)
    return jsonify(note)


# --- Read / View Post
@app.route('/note/<nid>/')
def readNote_route(nid):
    # note = readPost(id=nid).first()
    note = readPost(id=nid)
    return jsonify(note)


# --- List All Post
@app.route('/notes/')
def listNote_route():
    '''
    lim = request.args.get('limit')
    if isinstance(lim, str) != True:
        lim = 5
        print('xx')
    '''

    note = list()
    return jsonify(note)


# >>> CATCH ALL <<<
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You wanted path: %s' % path
