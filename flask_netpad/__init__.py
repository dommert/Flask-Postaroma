# Init File
# (C) Abstergo 2018
# Flask-Notepad v1.0-alpha

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
	some_service('localhost',5000,app)
