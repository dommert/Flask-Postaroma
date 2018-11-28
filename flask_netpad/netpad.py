# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## netpad.py [MongoDB logic]


from flask_netpad.models import db, Note


# Custom Error

def errorCode(code=404, msg='Object Not Found :( '):
    """
    Returns a custom error code in a dictionary
    :param code: Error Code 
    :param msg: Message to return
    :return: error
    """
    error = dict()
    error['code'] = code
    error['error'] = msg
    return error

def createDB(*args, **kwargs):
    try:
        return 'create db'
    except:
        errorCode()

# List Notes
def listNote(page=0, batch=40):
    try:
       # note = Note.objects.paginate(page=page, per_page=batch)
       note = Note.objects
       return note
    except:
        return errorCode()


# Read Note (id)
def readNote(*args, **kwargs):
    try:
        note = Note.objects(*args, **kwargs)
        print(note.count())
        return note
    except:
        return errorCode()

# New / Create Note
def newNote(slug, content, title=None, **kwargs):
    try:
        note = Note(slug=slug, title=title, content=content, fat={**kwargs})
        note.save()
        return note
    except:
        return errorCode(404, 'Note not Created!')

# Update Note
def updateNote(nid, noteData):
    try:
        # BlogPost.objects(id=post.id).update(title='Example Post')
        note=Note.objects(id=nid).get()
        note.content= noteData.content
        note.title= noteData.title
        note.slug= noteData.slug
        note.save()
        return note
    except:
        return errorCode(404, 'Note not Found!')


# Delete / Remove Note
def delNote(nid):
    # Soft Delete note
    try:
        note = Note.objects(_id=nid).first()
    except:
        return errorCode()
    return 'deleted'

