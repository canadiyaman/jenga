from django.db import models

from jenga.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    isbn13 = models.CharField(max_length=13)
