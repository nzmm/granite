import os
import os.path
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from granite.settings import STATIC_ROOT, STATIC_URL, G_TEXT_ROOT
from websites.models import Website
from granite.utils.cache import (
    FSDuplicate,
    hashed_filename,
    path_and_rename
)


class PlainTextAsset(models.Model, FSDuplicate):
    site = models.ForeignKey(Website)
    handle = models.CharField(max_length=48)
    text = models.TextField(default='')

    @property
    def fs_root(self):
        return G_TEXT_ROOT

    @property
    def fs_name(self):
        return hashed_filename(self, self.handle)

    @property
    def data(self):
        return self.text

    def url(self):
        return self.fs_full_path.replace(STATIC_ROOT, STATIC_URL.rstrip('/')).replace(os.sep, '/')
    url.short_description = 'URL'


# PlainTextAsset signal handlers
@receiver(post_save, sender=PlainTextAsset)
def plaintext_asset_post_save_handler(sender, **kwargs):
    kwargs['instance'].fs_dump()
    return


class FileAsset(models.Model):
    site = models.ForeignKey(Website)
    handle = models.CharField(max_length=48)
    file = models.FileField(upload_to=path_and_rename)

    def url(self):
        return '/'.join((STATIC_URL.rstrip('/'), 'media', 'files', os.path.split(self.file.name)[-1]))
    url.short_description = 'URL'

