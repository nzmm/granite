import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class Website(models.Model):
    name = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    authors = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlainTextAsset(models.Model):
    handle = models.CharField(max_length=48)
    text = models.TextField(default='')


class FileAsset(models.Model):
    handle = models.CharField(max_length=48)
    file = models.FileField(upload_to='assets')


class Template(models.Model):
    name = models.CharField(max_length=48)
    markup = models.TextField(default='')

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.name)

    @property
    def site(self):
        return Website.objects.get(pk=1)

    @property
    def fs_path(self):
        return "granitecore/templates/gen/%s" % self.site.handle

    @property
    def fs_name(self):
        return self.name.lower().replace(' ', '_')

    @property
    def fs_full_path(self):
        return '/'.join((self.fs_path, self.fs_name))

    @property
    def path(self):
        # django relative template path
        return '/'.join((self.site.handle, self.fs_name))


class Page(models.Model):

    NONE = 'NN'
    HOME = 'HM'
    ERROR = 'ER'

    PAGE_ROLES = (
        (NONE, 'Standard Page'),
        (HOME, 'Home Page'),
        (ERROR, 'Error Page'),
    )

    title = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    content = models.TextField(default='')
    template = models.ForeignKey(Template)
    role = models.CharField(max_length=2, choices=PAGE_ROLES, default=NONE)
    mauthor = models.ForeignKey(User)
    mtime = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(blank=True)
    publish_at = models.DateTimeField(blank=True)
    unpublish_at = models.DateTimeField(blank=True)

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.title)

    @property
    def site(self):
        return Website.objects.get(pk=1)


# Signal handlers
@receiver(post_save, sender=Template)
def template_post_save_handler(sender, **kwargs):
    template = kwargs['instance']

    if not os.path.exists(template.fs_path):
        os.makedirs(template.fs_path)

    with open(template.fs_full_path, 'w') as f:
        f.write(template.markup)
    return


@receiver(pre_delete, sender=Template)
def template_pre_delete_handler(sender, **kwargs):
    print(sender, kwargs)
    return
