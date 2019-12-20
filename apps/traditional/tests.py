import json
from unittest.mock import patch

from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse

from apps import helpers
from apps.bookmark.models import Bookmark
from apps.user.models import User


class TraditionalRenderPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_factory = RequestFactory()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    @patch.object(helpers.Client, 'search')
    def test_search_view(self, mocker):
        mocker.return_value = {
            "books": [
                {
                    "title": "Practical MongoDB",
                    "subtitle": "Architecting, Developing, and Administering MongoDB",
                    "isbn13": "9781484206485",
                    "price": "$35.20",
                    "image": "https://itbook.store/img/books/9781484206485.png",
                    "url": "https://itbook.store/books/9781484206485"
                },
                {
                    "title": "The Definitive Guide to MongoDB, 3rd Edition",
                    "subtitle": "A complete guide to dealing with Big Data using MongoDB",
                    "isbn13": "9781484211830",
                    "price": "$46.31",
                    "image": "https://itbook.store/img/books/9781484211830.png",
                    "url": "https://itbook.store/books/9781484211830",
                },
            ]
        }

        q = 'mongodb'
        response = self.client.get(f"{reverse(f'traditional:search')}?q={q}")
        self.assertEqual(response.status_code, 200)

    @patch.object(helpers.Client, 'book')
    def test_book_view(self, mocker):
        mocker.return_value = {
            "error": "0",
            "title": "Securing DevOps",
            "subtitle": "Security in the Cloud",
            "authors": "Julien Vehent",
            "publisher": "Manning",
            "isbn10": "1617294136",
            "isbn13": "9781617294136",
            "pages": "384",
            "year": "2018",
            "rating": "5",
            "desc": "An application running in the cloud can benefit from incredible efficiencies, but they come with unique security threats too. A DevOps team's highest priority is understanding those risks and hardening the system against them.Securing DevOps teaches you the essential techniques to secure your cloud ...",
            "price": "$26.98",
            "image": "https://itbook.store/img/books/9781617294136.png",
            "url": "https://itbook.store/books/9781617294136",
            "pdf": {
                "Chapter 2": "https://itbook.store/files/9781617294136/chapter2.pdf",
                "Chapter 5": "https://itbook.store/files/9781617294136/chapter5.pdf"
            }
        }

        isbn13 = '9781484206485'
        response = self.client.get(reverse(f'traditional:book', args=(isbn13,)))
        self.assertEqual(response.status_code, 200)

    @patch.object(helpers.Client, 'books')
    def test_books_view(self, mocker):
        mocker.return_value = {
            "books": [
                {
                    "title": "Practical MongoDB",
                    "subtitle": "Architecting, Developing, and Administering MongoDB",
                    "isbn13": "9781484206485",
                    "price": "$35.20",
                    "image": "https://itbook.store/img/books/9781484206485.png",
                    "url": "https://itbook.store/books/9781484206485"
                },
                {
                    "title": "The Definitive Guide to MongoDB, 3rd Edition",
                    "subtitle": "A complete guide to dealing with Big Data using MongoDB",
                    "isbn13": "9781484211830",
                    "price": "$46.31",
                    "image": "https://itbook.store/img/books/9781484211830.png",
                    "url": "https://itbook.store/books/9781484211830",
                },
            ]
        }
        response = self.client.get(reverse(f'traditional:books'))
        self.assertEqual(response.status_code, 200)

    def test_bookmarks_view(self):
        user = User.objects.create(
            first_name='test',
            last_name='user',
            username='testuser',
            email='a@a.com',
            ip='127.0.0.1'
        )
        user.set_password('1')
        user.save()

        Bookmark.objects.create(isbn13='9781788992879', user=user, data=json.dumps({
            "error": "0",
            "title": "Securing DevOps",
            "subtitle": "Security in the Cloud",
            "authors": "Julien Vehent",
            "publisher": "Manning",
            "isbn10": "1617294136",
            "isbn13": "9781617294136",
            "pages": "384",
            "year": "2018",
            "rating": "5",
            "desc": "An application running in the cloud can benefit from incredible efficiencies, but they come with unique security threats too. A DevOps team's highest priority is understanding those risks and hardening the system against them.Securing DevOps teaches you the essential techniques to secure your cloud ...",
            "price": "$26.98",
            "image": "https://itbook.store/img/books/9781617294136.png",
            "url": "https://itbook.store/books/9781617294136",
            "pdf": {
                "Chapter 2": "https://itbook.store/files/9781617294136/chapter2.pdf",
                "Chapter 5": "https://itbook.store/files/9781617294136/chapter5.pdf"
            }
        }))
        Bookmark.objects.create(isbn13='9781484211830', user=user, data=json.dumps({
            "error": "0",
            "title": "Securing DevOps",
            "subtitle": "Security in the Cloud",
            "authors": "Julien Vehent",
            "publisher": "Manning",
            "isbn10": "1617294136",
            "isbn13": "9781484211830",
            "pages": "384",
            "year": "2018",
            "rating": "5",
            "desc": "An application running in the cloud can benefit from incredible efficiencies, but they come with unique security threats too. A DevOps team's highest priority is understanding those risks and hardening the system against them.Securing DevOps teaches you the essential techniques to secure your cloud ...",
            "price": "$26.98",
            "image": "https://itbook.store/img/books/9781617294136.png",
            "url": "https://itbook.store/books/9781617294136",
            "pdf": {
                "Chapter 2": "https://itbook.store/files/9781617294136/chapter2.pdf",
                "Chapter 5": "https://itbook.store/files/9781617294136/chapter5.pdf"
            }
        }))
        Bookmark.objects.create(isbn13='9781484206485', user=user, data=json.dumps({
            "error": "0",
            "title": "Securing DevOps",
            "subtitle": "Security in the Cloud",
            "authors": "Julien Vehent",
            "publisher": "Manning",
            "isbn10": "1617294136",
            "isbn13": "9781484206485",
            "pages": "384",
            "year": "2018",
            "rating": "5",
            "desc": "An application running in the cloud can benefit from incredible efficiencies, but they come with unique security threats too. A DevOps team's highest priority is understanding those risks and hardening the system against them.Securing DevOps teaches you the essential techniques to secure your cloud ...",
            "price": "$26.98",
            "image": "https://itbook.store/img/books/9781617294136.png",
            "url": "https://itbook.store/books/9781617294136",
            "pdf": {
                "Chapter 2": "https://itbook.store/files/9781617294136/chapter2.pdf",
                "Chapter 5": "https://itbook.store/files/9781617294136/chapter5.pdf"
            }
        }))

        self.client.login(username='testuser', password='1')
        response = self.client.get(reverse('traditional:bookmarks'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    @patch.object(helpers.Client, 'book')
    def test_add_my_bookmarks_view(self, mocker):
        mocker.return_value = {
            "error": "0",
            "title": "Securing DevOps",
            "subtitle": "Security in the Cloud",
            "authors": "Julien Vehent",
            "publisher": "Manning",
            "isbn10": "1617294136",
            "isbn13": "9781617294136",
            "pages": "384",
            "year": "2018",
            "rating": "5",
            "desc": "An application running in the cloud can benefit from incredible efficiencies, but they come with unique security threats too. A DevOps team's highest priority is understanding those risks and hardening the system against them.Securing DevOps teaches you the essential techniques to secure your cloud ...",
            "price": "$26.98",
            "image": "https://itbook.store/img/books/9781617294136.png",
            "url": "https://itbook.store/books/9781617294136",
            "pdf": {
                "Chapter 2": "https://itbook.store/files/9781617294136/chapter2.pdf",
                "Chapter 5": "https://itbook.store/files/9781617294136/chapter5.pdf"
            }
        }

        user = User.objects.create(
            first_name='test',
            last_name='user',
            username='testuser',
            email='a@a.com',
            ip='127.0.0.1'
        )
        user.set_password('1')
        user.save()

        self.client.login(username='testuser', password='1')
        isbn13 = '9781484206485'
        response = self.client.get(f"{reverse('traditional:add_my_bookmarks')}?isbn13={isbn13}")
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(Bookmark.objects.filter(user=user), ['<Bookmark: Bookmark object (3)>'])
        self.client.logout()
