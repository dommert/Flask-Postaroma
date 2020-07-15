from flask import jsonify
from flask_restful import Resource


class Todo(Resource):
    def get(self, todo_id=None):
        return jsonify(test="12345", id=todo_id)


##  To Do CRUD

# Create
class Crud(Resource):
    def get(self, todo_id=None):
        return jsonify(method='get', test="12345", id=todo_id)

    def post(self, todo_id=None):
        return jsonify(method='post', test="12345", id=todo_id)

    def update(self, todo_id=None):
        return jsonify(method='update', test="12345", id=todo_id)

    def delete(self, todo_id=None):
        return jsonify(method='delete', test="12345", id=todo_id)

    def patch(self, todo_id=None):
        return jsonify(method='patch', test="12345", id=todo_id)


class List(Resource):
    def get(self, todo_id=None):
        return jsonify(method= "get", test="list dir", id=todo_id)
