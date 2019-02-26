from django.http.response import JsonResponse
from django.shortcuts import render

from apps.bookmark.models import Bookmark
from apps.helpers import get_adapter
from apps.traditional.serializers import BookListSerializer, BookmarkListSerializer, \
    BookSerializer


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


def search(request):
    q, page = request.GET.get('q', ""), request.GET.get('page', 1)
    results = get_adapter().search(q, page)

    serializer = BookListSerializer(results, request)
    context = {
        "books": serializer.data,
    }
    return render(request, 'pages/search.html', context)


def book(request, isbn13):
    book = get_adapter().book(isbn13)
    serializer = BookSerializer(book, request)

    context = {
        "book": serializer.data
    }
    return render(request, 'pages/book.html', context)


def books(request):
    page = request.GET.get('page', 1)
    results = get_adapter().books(page)

    serializer = BookListSerializer(results, request)
    context = {
        "books": serializer.data,
    }
    return render(request, 'pages/books.html', context)


def bookmarks(request):
    queryset = request.user.bookmark_set.all()
    serializer = BookmarkListSerializer(queryset)

    context = {
        "bookmarks": serializer.data
    }
    return render(request, 'pages/bookmarks.html', context)


def add_my_bookmarks(request):
    isbn13 = request.GET.get('isbn13')
    book = get_adapter().book(isbn13)
    success, message = Bookmark.add_my_bookmarks(request.user, book)

    response = {
        "success": success,
        "message": message
    }
    return JsonResponse(response)
