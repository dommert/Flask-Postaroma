# Flask-Postaroma
# version 1.0-alpha
# (C) Abstergo 2020
## posts.py [MongoDB logic]


from flask_postaroma.models import Post, Blog, MetaData




# Should this be a CLASS

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
        test = Post
        note = test.objects(**kwargs)
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
        #note = Post.objects.get(id=nid)
        note = Post.objects(id=nid).first()
        return note
    except:
        return errorCode()


# == New / Create Post
def create(slug, **kwargs):
    try:
        note = Post(slug=slug, **kwargs)
        note.save()
        return note
    except Exception as ex:
        return errorCode(404, str(ex))


# Update Post
def update(nid, postData):
    try:

        post = Post.objects(id=nid).update(**postData)
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






############

def createBlog(content=None, title=None, **kwargs):
    try:
        # note = Post(slug=slug, title=title, content=content, fat={**kwargs})
        #d = Data(title=title)
        note = Blog(content=content, title=title)
        #d.save()
        note.save()
        return note
    except:
        return errorCode(404, 'Post not Created!')



# ==  List Notes
def listBlog(**kwargs):
    try:
        blog = Blog.objects(**kwargs)
        return blog
    except:
        return errorCode()

