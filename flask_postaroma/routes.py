# Flask-Postaroma
# version 1.0-alpha
# (C) Abstergo 2020
from flask_postaroma.app import api, app
from flask_postaroma.router import posts
from flask_postaroma.router.blogs import BlogCrud, BlogList


@app.route('/')
def index():
    return 'Hello World!'


# Post Example
api.add_resource(posts.List, '/posts/')
api.add_resource(posts.Crud, '/post/<todo_id>')


# Blog
api.add_resource(BlogList, '/blogs/')




# >>> CATCH ALL <<<
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You wanted path: %s' % path