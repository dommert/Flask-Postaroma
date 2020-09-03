# Flask-Postaroma
# version 1.0-alpha
# (C) Abstergo 2020
## models.py

# Imports
import datetime
from flask_mongoengine import MongoEngine, QuerySet
from flask_postaroma.app import app

# Declares
db = MongoEngine()
db.init_app(app)


# Not Deleted Class
class DeletedQuery(QuerySet):
    def active(self):
        return self.filter(deleted=False)


class MetaData(db.EmbeddedDocument):
    created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    creator = db.StringField()
    deleted = db.BooleanField(default=False)


# Post Model
class Post(db.Document):
    metaData = db.EmbeddedDocumentField(MetaData)
    slug = db.StringField(unique=True, require=True)
    title = db.StringField(max_length=60)
    content = db.StringField()
    meta = {'queryset_class': DeletedQuery, 'allow_inheritance': True}
    #created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    #author = db.StringField(max_length=60, require=True)
    #deleted = db.BooleanField(default=False)
    fat = db.DictField()




class Page(db.Document):
    title = db.StringField(max_length=120)
    created = db.DateTimeField(default=datetime.datetime.now(), require=True)
    meta = {'allow_inheritance': True}

class Blog(Page):
    content = db.StringField()


class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

class Content(db.EmbeddedDocument):
    text = db.StringField()
    lang = db.StringField(max_length=3)

class Posting(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=30))
    content = db.EmbeddedDocumentField(Content)
