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
    data = dict()
    data['code'] = code
    data['error'] = msg
    return data

# ==
def createDB(*args, **kwargs):
    try:
        return 'create db'
    except:
        errorCode()

# ==  List Notes
def listNote(**kwargs):
    try:
        note = Note.objects(**kwargs)
        return note
    except:
        return errorCode()


# == Pagination Note
def pageNote(page=1, per_page=40, **kwargs):
    try:
       note = Note.objects(deleted=False).paginate(page=page, per_page=per_page)
       data = dict()
       data['page_current'] = note.page
       data['page_total'] = note.pages
       data['per_page'] = note.per_page
       data['total_items'] = note.total
       data['data'] = note.items
       return data
    except:
        note = errorCode()
        return note



# ==  Read Note
def readNote(**kwargs):
    try:
        note = Note.objects(**kwargs)
        return note
    except:
        return errorCode()


# == New / Create Note
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
        note = Note.objects(id=nid).update(deleted=True)
        data = dict()
        data['total'] = note
        data['id'] = nid
        return data
    except:
        return errorCode()


