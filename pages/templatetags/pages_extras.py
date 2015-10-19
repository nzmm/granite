__author__ = 'Matthew'

from django import template
from django.utils.safestring import mark_safe
from assets.models import FileAsset, PlainTextAsset

register = template.Library()


@register.filter
def asset_url(site, handle):
    try:
        asset = PlainTextAsset.objects.get(site=site, handle=handle)
    except PlainTextAsset.DoesNotExist:
        try:
            asset = FileAsset.objects.get(site=site, handle=handle)
        except FileAsset.DoesNotExist:
            return None
    return mark_safe(asset.url())


@register.filter
def stylesheet_tag(url):
    return mark_safe('<link href="%s" rel="stylesheet" type="text/css">' % url)


@register.filter
def script_tag(url):
    return mark_safe('<script src="%s" type="text/javascript"></script>' % url)


@register.filter
def img_tag(url, attrs=''):
    return mark_safe('<img src="%s" %s>' % (url, attrs))


@register.filter
def iendswith(a, b):
    return a.lower().endswith(b.lower())
