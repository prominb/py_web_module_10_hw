from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponse

from .models import Author, Quote
from .forms import UserRegistrationForm, AuthorForm, QuoteForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            if user is not None:
                login(request, user)
                messages.info(request, 'Registration has been successful!')
                return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have logged out of your account!')
    return redirect('/')


@login_required
def add_author(request):
    author_instance = Author.objects.first()
    form = AuthorForm(instance=author_instance)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect(to='/')
    return render(request, 'users/add_author.html', context={"form": form})


@login_required
def add_quote(request):
    quote_instance = Quote.objects.first()
    form = QuoteForm(instance=quote_instance)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect(to='/page/1')
    return render(request, 'users/add_quote_author.html', context={"form": form})
