from flask import Flask, request, jsonify
import datetime
from flask_mongoengine import MongoEngine

app = Flask(__name__)
# Import Config
app.config.from_pyfile('app.cfg')

# Declares
db = MongoEngine()
db.init_app(app)


# Post Model
class Note(db.DynamicDocument):
    created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    slug = db.StringField(unique=True, require=True)
    title = db.StringField(max_length=60)
    author = db.StringField(max_length=60, require=True)
    content = db.StringField()
    deleted = db.BooleanField(default=False)
    fat = db.DictField()


# Custom Error
def errorCode(code=404, msg='Object Not Found :( '):
    error = dict()
    error['code'] = code
    error['error'] = msg
    return error


def createDB():
    return 'DB Created! (hopefully)'


# List Notes
def listNote():
    try:
        note = Note.objects.all()
        return note
    except:
        return errorCode()


@app.route('/')
def index():
    return 'Hello World!'


# List Post
@app.route('/note/')
def listNote_route():
    lim = request.args.get('limit')
    if isinstance(lim, str) == True:
        lim = 5
    note = listNote().limit(lim)
    return jsonify(note)


if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'],
            port=app.config['SERVER_PORT'],
            debug=app.config['DEBUG'])
