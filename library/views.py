from datetime import datetime

from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, Author, Publisher
from .forms import AddPublisherForm, AddBookForm, AddAuthorForm
# Create your views here.


def all_books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'all_books.html', {'books': page_object})


def book_info(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'book_info.html', {'book': book, 'authors': authors, 'publishers': publishers})


def new_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddBookForm()
    return render(request, 'add_new.html', {'form': form})


def new_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddAuthorForm()
    return render(request, 'add_new.html', {'form': form})


def new_publisher(request):
    if request.method == 'POST':
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddPublisherForm()
    return render(request, 'add_new.html', {'form': form})


def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all_books')
        else:
            return HttpResponse('Неправильные учетные данные')

    return render(request, 'login.html')


