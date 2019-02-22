from django.shortcuts import render

from apps.helpers import get_adapter


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


def search(request):
    q = request.GET.get('q', "")
    adapter = get_adapter()
    results = adapter.search(q)
    return render(request, 'pages/search.html', results)


def book(request, isbn13):
    adapter = get_adapter()
    result = adapter.book(isbn13)
    return render(request, 'pages/book.html', result)


def books(request):
    adapter = get_adapter()
    result = adapter.books()
    return render(request, 'pages/books.html', result)
