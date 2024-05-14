from bson.objectid import ObjectId

from django import template

# from ..utils import get_mongodb

from ..models import Author

register = template.Library()


def get_author(id_):
    # db = get_mongodb()
    # author = db.authors.find_one({'_id': ObjectId(id_)})
    # return author['fullname']

    author = Author.objects.get(id=id_)  # TypeError: Field 'id' expected a number but got <Author: Albert Einstein>.
    # author = Author.objects.get(pk=id_)
    # author = Author.objects
    # return author['fullname']
    return author


register.filter('author', get_author)
