from flask_postaroma.app import api
from flask_postaroma.router import todo

api.add_resource(todo.Todo, '/test')

# To Do
api.add_resource(todo.List, '/todos/')
api.add_resource(todo.Crud,  '/todo/<todo_id>')
