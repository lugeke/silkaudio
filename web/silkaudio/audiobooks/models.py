from django.db import models
from django.contrib.auth.models import AbstractUser


class Audiobook(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    description = models.TextField()
    chapters = models.TextField(blank=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class User(AbstractUser):
    histories = models.ManyToManyField(Audiobook, through='History')


class History(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE,)
    audiobook = models.ForeignKey('Audiobook', on_delete=models.CASCADE,)
    progress = models.FloatField(default=0)
    recentListen = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{ab.user} {ab.audiobook} {ab.progress}s'.format(ab=self)
