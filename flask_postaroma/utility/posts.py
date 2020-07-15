# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## old_routes.py


from flask import request, jsonify
from flask_postaroma.app import app
from flask_postaroma.posts import *


def index():
    return 'Hello World!'


# ==== Notes Routes =====

# --- List Post
def list():
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

    print(page,perpage)
    note = pagePost(page=page, per_page=perpage)
    return jsonify(note)


# --- Read / View Post
def readNote_route(nid):
    #note = readPost(id=nid).first()
    note = readPost(id=nid)
    return jsonify(note)


# --- List All Post
def listNote_route():
    '''
    lim = request.args.get('limit')
    if isinstance(lim, str) != True:
        lim = 5
        print('xx')
    '''

    note = list()
    return jsonify(note)