from flask_postaroma.app import api
from flask_postaroma.router import todo


# To Do Example
api.add_resource(todo.List, '/todos/')
api.add_resource(todo.Crud,  '/todo/<todo_id>')
