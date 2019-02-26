from json import dumps

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from jenga.settings import AUTH_USER_MODEL


class Bookmark(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    isbn13 = models.CharField(max_length=13)
    data = models.TextField(blank=True, null=True)

    @classmethod
    def add_my_bookmarks(cls, user, data):
        isbn13 = data.get('isbn13')
        if not isbn13:
            return False, _("You must select a book first.")

        if cls.objects.filter(user=user, isbn13=isbn13).exists():
            return False, _("This book already added to your bookmarks.")

        cls.objects.create(user=user, isbn13=isbn13, data=dumps(data))
        return True, _("Successfully added to your bookmarks")
