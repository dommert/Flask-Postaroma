from flask import jsonify
from flask_restful import Resource


class Todo(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


##  To Do CRUD

# Create
class Create(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


# Read
class Read(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


# Update
class Update(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


# Delete
class Delete(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


# List
class List(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)
