from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .utils import get_mongodb
from .forms import TagForm

# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', {'quotes': quotes_on_page})

# def add_tag(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='noteapp:main')
#         else:
#             return render(request, 'noteapp/tag.html', {'form': form})

#     return render(request, 'noteapp/tag.html', {'form': TagForm()})
