import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class FSDuplicate(object):
    TEMPLATE_REL_ROOT = ''
    FS_ROOT = ''
    handle = ''

    @property
    def site(self):
        return Website.objects.get(pk=1)

    @property
    def fs_path(self):
        return '/'.join((self.FS_ROOT, self.site.handle))

    @property
    def fs_name(self):
        return self.handle.lower().replace(' ', '_')

    @property
    def fs_full_path(self):
        return '/'.join((self.fs_path, self.fs_name))

    @property
    def path(self):
        # django relative template path
        return '/'.join(p for p in (self.TEMPLATE_REL_ROOT, self.site.handle, self.fs_name) if p.strip())

    @property
    def data(self):
        raise NotImplementedError('Any class inheriting FSDuplicate should implement their own data property')

    def fs_dump(self):
        if not os.path.exists(self.fs_path):
            os.makedirs(self.fs_path)
        with open(self.fs_full_path, 'w') as f:
            f.write(self.data)
        return


class Website(models.Model):
    name = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    authors = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlainTextAsset(models.Model, FSDuplicate):
    FS_ROOT = 'static/gen'

    handle = models.CharField(max_length=48)
    text = models.TextField(default='')

    @property
    def data(self):
        return self.text


# PlainTextAsset signal handlers
@receiver(post_save, sender=PlainTextAsset)
def plaintext_asset_post_save_handler(sender, **kwargs):
    kwargs['instance'].fs_dump()
    return


class FileAsset(models.Model, FSDuplicate):
    handle = models.CharField(max_length=48)
    file = models.FileField(upload_to='assets')

    @property
    def data(self):
        return self.file


class Template(models.Model, FSDuplicate):
    FS_ROOT = 'granitecore/templates/gen'

    handle = models.CharField(max_length=48)
    markup = models.TextField(default='')

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.handle)

    @property
    def data(self):
        return self.markup


# Template signal handlers
@receiver(post_save, sender=Template)
def template_post_save_handler(sender, **kwargs):
    kwargs['instance'].fs_dump()
    return


@receiver(pre_delete, sender=Template)
def template_pre_delete_handler(sender, **kwargs):
    print(sender, kwargs)
    return


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

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.title)

    @property
    def site(self):
        return Website.objects.get(pk=1)

