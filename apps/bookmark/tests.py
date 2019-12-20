from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from apps.bookmark.models import Bookmark
from apps.user.models import User


class BookmarkModelTestCase(TestCase):
    def test_crud_bookmark_model(self):
        # create
        user = User.objects.create(
            first_name='test',
            last_name='user',
            username='testuser',
            email='a@a.com',
            ip='127.0.0.1'
        )
        bookmark = Bookmark.objects.create(isbn13='9781788992879', user=user)

        # read
        self.assertEqual(bookmark.id, bookmark.pk)

        # update
        bookmark.isbn13 = '1111111111111'
        bookmark.save()
        self.assertEqual(Bookmark.objects.last().isbn13, '1111111111111')

        # delete
        delete_bookmark = bookmark.delete()
        self.assertEqual((1, {'bookmark.Bookmark': 1}), delete_bookmark)

    def test_add_my_bookmarks(self):
        user = User.objects.create(
            first_name='test',
            last_name='user',
            username='testuser',
            email='a@a.com',
            ip='127.0.0.1'
        )
        data = {}

        success, message = Bookmark.add_my_bookmarks(user, data)

        self.assertFalse(success)
        self.assertEqual(message, _("You must select a book first."))
        self.assertQuerysetEqual(Bookmark.objects.all(), [])

        data.update({'isbn13': '1234567891123'})
        success, message = Bookmark.add_my_bookmarks(user, data)

        self.assertTrue(success)
        self.assertEqual(message, _("Successfully added to your bookmarks"))
        self.assertQuerysetEqual(Bookmark.objects.all(), ['<Bookmark: Bookmark object (1)>'])

        success, message = Bookmark.add_my_bookmarks(user, data)

        self.assertFalse(success)
        self.assertEqual(message, _("This book already added to your bookmarks."))
        self.assertQuerysetEqual(Bookmark.objects.all(), ['<Bookmark: Bookmark object (1)>'])
