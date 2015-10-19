import os
import os.path
from PIL import Image
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from granite.settings import STATIC_URL, G_TEXT_ROOT, G_FILE_ROOT
from granite.core.objects import FSDuplicate
from websites.models import Website


class PlainTextAsset(models.Model, FSDuplicate):
    ASSET_TYPE_NAME = 'text'
    FS_ROOT = G_TEXT_ROOT

    site = models.ForeignKey(Website)
    handle = models.CharField(max_length=48)
    text = models.TextField(default='')

    @property
    def data(self):
        return self.text

    def url(self):
        return '/'.join((STATIC_URL.rstrip('/'), 'media', 'plaintext', self.handle))


# PlainTextAsset signal handlers
@receiver(post_save, sender=PlainTextAsset)
def plaintext_asset_post_save_handler(sender, **kwargs):
    kwargs['instance'].fs_dump()
    return


class FileAsset(models.Model):
    ASSET_TYPE_NAME = 'file'

    site = models.ForeignKey(Website)
    handle = models.CharField(max_length=48)
    file = models.FileField(upload_to=G_FILE_ROOT)

    def url(self):
        return '/'.join((STATIC_URL.rstrip('/'), 'media', 'files', os.path.split(self.file.name)[-1]))
    url.short_description = 'URL'

    def thumbnail_small(self):
        try:
            Image.open(self.file)
        except OSError:
            return ('<p style="text-align:center;width:64px;"><img src="/static/granite/img/non_image_file.png" '
                    'height="36"></p>')

        return '<p style="text-align:center;width:64px;"><img src="%s" height="36"></p>' % self.url()
    thumbnail_small.short_description = 'File preview'
    thumbnail_small.allow_tags = True

    def thumbnail_large(self):
        try:
            Image.open(self.file)
        except OSError:
            return ('<p style="text-align:center;max-width:128px;padding:15px;">'
                    '<img src="/static/granite/img/non_image_file.png" height="36"></p>')

        return ('<p style="text-align:center;max-width:128px;padding:15px;">'
                '<img src="%s" height="84"></p>' % self.url())
    thumbnail_large.short_description = 'File preview'
    thumbnail_large.allow_tags = True
