import requests

from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404


class Client(object):
    URL = "https://api.itbook.store/1.0"

    def validate_response(self, response):
        if response.status_code != 200:
            raise Http404

    def byte_to_dict(self, response):
        from json import loads
        return loads(response.decode())

    def call(self, path, method, data):
        url = "%s/%s" % (self.URL, path)
        r = getattr(requests, method)(url, data)
        self.validate_response(r)
        return self.byte_to_dict(r.content)

    def search(self, q):
        return self.call('search/%s' % q, 'get', {})

    def book(self, isbn13):
        return self.call('books/%s' % isbn13, 'get', {})

    def books(self):
        return self.call('new', 'get', {})


class Adapter(object):

    def __init__(self):
        self.client = Client()

    def paginate(self, objects, page):
        paginator = Paginator(objects, settings.DEFAULT_PER_PAGE_LIMIT, page)
        return paginator.page(page)

    def search(self, q, page=1, paginated=True):
        response = self.client.search(q)
        books = response['books']
        if paginated:
            books = self.paginate(books, page)
        return {
            "books": books
        }

    def book(self, isbn13):
        response = self.client.book(isbn13)
        return {
            "book": response
        }

    def books(self, page=1, paginated=True):
        response = self.client.books()
        books = response['books']
        if paginated:
            books = self.paginate(books, page)
        return {
            "books": books
        }


def get_adapter():
    return Adapter()
