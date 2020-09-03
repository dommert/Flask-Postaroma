# Flask-Postaroma
# version 1.0-alpha
# (C) Abstergo 2020
from flask import jsonify, request
from flask_restful import Resource
from flask_postaroma.utility import posts


##  To Do CRUD

# Create
class Crud(Resource):
    def get(self, pid=None):
        try:
            # Post Record
            p = posts.read(pid)
            return jsonify(method='get', post=p)
        except Exception as ex:
            return jsonify(error="Error: Could not fetch Post", message=str(ex))

    def post(self, pid=None):
        req = request.get_json()
        #slug = req['slug']
        #posts.create()
        return jsonify(method='post', test="12345", id=pid)

    def update(self, pid=None):


        req = request.get_json()
        posts.update(pid, req)

        return jsonify(method='update', test="12345", id=pid)

    def delete(self, pid=None):
        return jsonify(method='delete', test="12345", id=pid)

    def patch(self, pid=None):
        return jsonify(method='patch', test="12345", id=pid)


class List(Resource):
    def get(self, todo_id=None):
        p = posts.list()
        return jsonify(method="get", test="list dir", posts=p)
