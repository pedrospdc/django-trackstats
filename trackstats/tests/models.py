from django.db import models
from django.utils import timezone


class Comment(models.Model):
    user = models.ForeignKey('auth.User')
    timestamp = models.DateTimeField(default=timezone.now)


class Publication(models.Model):
    title = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=timezone.now)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
