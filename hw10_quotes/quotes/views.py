from bson.objectid import ObjectId

from django.shortcuts import render
from django.core.paginator import Paginator

# from django.http import HttpResponse

from .utils import get_mongodb
# from .models import Quote

# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', {'quotes': quotes_on_page})

def author_details(request, id_):
    db = get_mongodb()
    author = db.authors.find_one({"_id": ObjectId(id_)})
    return render(request, "quotes/author_details.html", context={"author": author})

