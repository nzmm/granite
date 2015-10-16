__author__ = 'Matthew'

from django import template
from granitecore.models import Website

register = template.Library()


@register.filter
def asset_url(asset_handle):
    site = Website.objects.get(pk=1)
    return "/static/gen/%s/%s" % (site.handle, asset_handle)


@register.filter
def stylesheet_tag(url):
    return '<link href="%s" rel="stylesheet" type="text/css">' % url


@register.filter
def script_tag(url):
    return '<script src="%s" type="text/javascript"></script>' % url


@register.filter
def img_tag(url, attrs=''):
    return '<img src="%s" %s>' % (url, attrs)
