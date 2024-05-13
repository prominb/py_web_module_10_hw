from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb
# from .models import Quote

# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    # quotes = Quote.objects.all()  # Exception Type: TypeError
# Exception Value: id must be an instance of (bytes, str, ObjectId), not <class 'quotes.models.Author'>
# 10 <span>by <small class="author" itemprop="author">{{ quote.author|author }}</small>
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', {'quotes': quotes_on_page})
