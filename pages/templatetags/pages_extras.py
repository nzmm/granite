__author__ = 'Matthew'

from django import template
from django.utils.safestring import mark_safe
from granite.settings import G_URL_PATH
from assets.models import FileAsset, PlainTextAsset
from pages.models import Page

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
def page_link(site, page_handle):
    pages = Page.objects.filter(site=site, published=True, handle__contains=page_handle)
    if pages:
        page_handle = pages.first().handle
    else:
        page_handle = '/pages/nosuchpage/'
    if not page_handle.startswith('pages/'):
        page_handle = '/pages/%s' % page_handle
    if not page_handle.endswith('/'):
        page_handle += '/'
    if site.link_with_site_handle:
        return '%s/%s%s' % (G_URL_PATH, site.handle, page_handle)
    return page_handle


@register.filter
def iendswith(a, b):
    return a.lower().endswith(b.lower())
