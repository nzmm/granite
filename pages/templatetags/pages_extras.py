__author__ = 'Matthew'

import os.path
from django import template
from django.utils.safestring import mark_safe
from granite.settings import STATIC_URL
from assets.models import FileAsset, PlainTextAsset

register = template.Library()


@register.filter
def asset_url(site, handle):
    mode = 'text'
    try:
        asset = PlainTextAsset.objects.get(site=site, handle=handle)
    except PlainTextAsset.DoesNotExist:
        try:
            asset = FileAsset.objects.get(site=site, handle=handle)
            mode = 'file'
        except FileAsset.DoesNotExist:
            return None
    if mode == 'file':
        return mark_safe('/'.join((STATIC_URL.rstrip('/'), os.path.split(asset.file.name)[-1])))
    return mark_safe('/'.join((STATIC_URL.rstrip('/'), asset.handle)))


@register.filter
def stylesheet_tag(url):
    return mark_safe('<link href="%s" rel="stylesheet" type="text/css">' % url)


@register.filter
def script_tag(url):
    return mark_safe('<script src="%s" type="text/javascript"></script>' % url)


@register.filter
def img_tag(url, attrs=''):
    return mark_safe('<img src="%s" %s>' % (url, attrs))
