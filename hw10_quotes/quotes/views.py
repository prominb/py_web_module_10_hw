from bson.objectid import ObjectId

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm
from .models import Quote, Tag

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

def find_by_tag(request, tag):
    db = get_mongodb()
    quotes_by_tag = db.quotes.find({"tags": str(tag)})
    return render(request, 'quotes/tag.html', {'quotes': quotes_by_tag})

@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:main")
    else:
        form = AuthorForm()

    return render(request, "quotes/add_author.html", {"form": form})

@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data["quote"]
            author = form.cleaned_data["author"]

            tags_input = str(form.cleaned_data["tags"])

            tags_list = [tag.strip() for tag in tags_input.split(",")]

            tags = [
                Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tags_list
            ]

            quote = Quote(quote=quote_text, author=author)
            quote.save()
            # for tag in tags:
            #     quote.tags.add(tag)
            tags_to_add = [tag for tag in tags if tag not in quote.tags.all()]
            quote.tags.add(*tags_to_add)

            return redirect(reverse("quotes:main"))

    else:
        form = QuoteForm()

    return render(request, "quotes/add_quote.html", {"form": form})

@login_required
def delete_quote(request, id_):
    try:
        quote = Quote.objects.get(id=id_)
        quote.delete()
    except Quote.DoesNotExist:
        pass
    return redirect("quotes:main")
