from flask import jsonify
from flask_restful import Resource


class Todo(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


class Read(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)


class Create(Resource):
    def get(self, todo_id=False):
        return jsonify(test="12345", id=todo_id)