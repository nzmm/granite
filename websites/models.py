from django.db import models
from django.utils.safestring import mark_safe


class Website(models.Model):
    name = models.CharField(max_length=100)
    hosts = models.CharField(max_length=100, default='http://127.0.0.1:8000/')
    handle = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default='', blank=True)
    authors = models.CharField(max_length=255, default='', blank=True)
    copyright = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.name

    def toplevel_pages(self):
        from pages.models import Page
        return Page.objects.filter(site=self, role__gte=1000, published=True)

    def link_list(self):
        return [mark_safe('<a href="%s">%s</a>' % (p.handle, p.title)) for p in self.toplevel_pages()]
