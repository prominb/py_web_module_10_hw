from django.shortcuts import render
from django.core.paginator import Paginator

from django.http import HttpResponse

from .utils import get_mongodb
from .models import Quote

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


# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_quotes_list = Quote.objects.order_by('created_at')[:5]
#     output = ', '.join([q.quote for q in latest_quotes_list])
#     return HttpResponse(output)
#     # return HttpResponse(latest_question_list)
#     # return HttpResponse([q.quote + "\n" for q in latest_quotes_list])

# def detail(request, quotes_id):
#     return HttpResponse("You're looking at quote %s." % quotes_id)

# def results(request, quotes_id):
#     response = "You're looking at the results of quote %s."
#     return HttpResponse(response % quotes_id)

# def index(request):
#     latest_quotes_list = Quote.objects.order_by('created_at')[:15]
#     context = {'latest_quotes_list': latest_quotes_list}
#     return render(request, 'quotes/index.html', context)
