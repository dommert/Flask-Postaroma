# Flask-Postaroma
# version 1.0-alpha
# (C) Abstergo 2018
## models.py

# Imports
import datetime
from flask_mongoengine import MongoEngine, QuerySet, Document
from flask_postaroma.app import app

# Declares
db = MongoEngine()
db.init_app(app)


# Not Deleted Class
class DeletedQuery(QuerySet):
    def active(self):
        return self.filter(deleted=False)



class Page(Document):
    title = db.StringField(max_length=120)
    created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    meta = {'allow_inheritance': True}

class Blog(Page):
    content = db.StringField()


# Post Model
class Post(Document):
    slug = db.StringField(unique=True, require=True)
    title = db.StringField(max_length=60)
    content = db.StringField()
    fat = db.DictField()
    meta = {'queryset_class': DeletedQuery, 'allow_inheritance': True}
    created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    author = db.StringField(max_length=60, require=True)
    deleted = db.BooleanField(default=False)
