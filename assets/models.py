import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from granite.core.objects import FSDuplicate
from websites.models import Website


class PlainTextAsset(models.Model, FSDuplicate):
    ASSET_TYPE_NAME = 'text'
    FS_ROOT = os.path.join('assets', 'static')

    site = models.ForeignKey(Website)
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


class FileAsset(models.Model):
    ASSET_TYPE_NAME = 'file'

    site = models.ForeignKey(Website)
    handle = models.CharField(max_length=48)
    file = models.FileField(upload_to='assets/static')
