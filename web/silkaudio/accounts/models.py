from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    histories = models.ManyToManyField('audiobooks.Audiobook',
                                       through='audiobooks.History')
