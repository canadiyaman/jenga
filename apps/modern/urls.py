from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.modern.views import BookSearchAPIView, BookDetailAPIView, BookListAPIView

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url('^books$', BookListAPIView.as_view(), 'books'),
    url('^books/(?P<isbn13>[^/.]+)$', BookDetailAPIView.as_view(), name='book_details'),
    url('^books/search$', BookSearchAPIView.as_view(), name='search'),
]

urlpatterns += router.urls
