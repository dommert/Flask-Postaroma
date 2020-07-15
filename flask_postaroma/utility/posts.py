# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## posts.py [MongoDB logic]


from flask_postaroma.models import Post


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


# ==  List Notes
def list(**kwargs):
    try:
        note = Post.objects(**kwargs)
        return note
    except:
        return errorCode()


# == Pagination Post
def paginate(page=1, per_page=40, **kwargs):
    try:
        note = Post.objects(deleted=False).paginate(page=page, per_page=per_page)
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


# ==  Read Post
def read(nid):
    try:
        note = Post.objects(id=nid)
        return note
    except:
        return errorCode()


# == New / Create Post
def create(slug, content, title=None, **kwargs):
    try:
        # note = Post(slug=slug, title=title, content=content, fat={**kwargs})
        note = Post(slug=slug, title=title, content=content)

        note.save()
        return note
    except:
        return errorCode(404, 'Post not Created!')


# Update Post
def update(nid, postData):
    try:
        # BlogPost.objects(id=post.id).update(title='Example Post')
        post = Post.objects(id=nid).get()
        post.content = postData.content
        post.title = postData.title
        post.slug = postData.slug
        post.save()
        return post
    except:
        return errorCode(404, 'Post not Found!')


# Delete / Remove Post
def delete(nid):
    # Soft Delete Post
    try:
        post = Post.objects(id=nid).update(deleted=True)
        data = dict()
        data['total'] = post
        data['id'] = nid
        return data
    except:
        return errorCode()
