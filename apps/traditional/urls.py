from django.conf.urls import url

from apps.traditional.views import home, search, book, books

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search$', search, name="search"),
    url(r'^books/(?P<isbn13>[^/.]+)$', book, name='book'),
    url(r'^books$', books, name='books')
]
