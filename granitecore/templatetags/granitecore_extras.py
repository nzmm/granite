__author__ = 'Matthew'

from django import template
from django.utils.safestring import mark_safe
from granite.settings import STATIC_URL
from granitecore.models import FileAsset, PlainTextAsset

register = template.Library()


@register.filter
def asset_url(site, asset_handle):
    for asset in PlainTextAsset.objects.filter(site=site, handle=asset_handle):
        if asset:
            return '/'.join((STATIC_URL.rstrip('/'), asset.handle))
    return None


@register.filter
def stylesheet_tag(url):
    return mark_safe('<link href="%s" rel="stylesheet" type="text/css">' % url)


@register.filter
def script_tag(url):
    return mark_safe('<script src="%s" type="text/javascript"></script>' % url)


@register.filter
def img_tag(url, attrs=''):
    return mark_safe('<img src="%s" %s>' % (url, attrs))
