# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## netpad.py [MongoDB logic]


from flask_netpad.models import db, Note


# Custom Error
def errorCode(code=404, msg='Object Not Found :( '):
    error = dict()
    error['code'] = code
    error['error'] = msg
    return error


# List Notes
def listNote():
    try:
        note = Note.objects.all()
        return note
    except:
        return errorCode()


# Read Note (id)
def readNote(nid):
    try:
        note = Note.objects(id=nid)
        print(note.count())
        return note
    except:
        return errorCode()

# New / Create Note
def newNote(slug, content, title=None, **kwargs)
    try:
        note = Note(slug=slug, title=title, content=content, fat={**kwargs})
        return note
    except:
        return errorCode(404, 'Note not Created!')

# Update Note

# Delete / Remove Note

