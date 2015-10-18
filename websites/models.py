from django.db import models


class Website(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100, default='http://127.0.0.1:8000/')
    handle = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default='', blank=True)
    authors = models.CharField(max_length=255, default='', blank=True)
    copyright = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.name
