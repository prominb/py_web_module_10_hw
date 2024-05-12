from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from .utils import get_mongodb
from .models import Author, Tag
# from .forms import TagForm

# Create your views here.
class AuthorView(DetailView):
    model = Author
    template_name = 'quotes/about_author.html'
    context_object_name = 'author'
    slug_field = 'fullname'
    slug_url_kwarg = 'author'

class QuotesByTagView(DetailView):
    model = Tag
    template_name = 'quotes/tag.html'
    context_object_name = 'tag'
    slug_field = 'name'
    slug_url_kwarg = 'quote'


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', {'quotes': quotes_on_page})
