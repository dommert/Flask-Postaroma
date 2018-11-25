# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## app.py

from flask import Flask

app = Flask(__name__)
# Import Config
app.config.from_pyfile('app.cfg')

from flask_netpad.routes import *

if __name__ == '__main__':
	app.run(host=app.config['SERVER_HOST'],
			port=app.config['SERVER_PORT'],
			debug=app.config['DEBUG'])
