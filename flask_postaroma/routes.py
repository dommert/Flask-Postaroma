
from flask_postaroma.app import api
from flask_postaroma.router import todo

#api.add_resource(TodoList, '/todos')
api.add_resource(todo.Todo, '/test')
api.add_resource(todo.Read, '/todos/', '/todos/<todo_id>')
