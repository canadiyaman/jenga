from django.conf.urls import url

from apps.traditional import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search$', views.search, name="search"),
    url(r'^books/(?P<isbn13>[^/.]+)$', views.book, name='book'),
    url(r'^books$', views.books, name='books'),
    url(r'^bookmarks$', views.bookmarks, name='bookmarks'),
    url(r'^ajax/add-my-bookmarks$', views.add_my_bookmarks, name='add_my_bookmarks')
]
