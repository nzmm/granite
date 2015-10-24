__author__ = 'matthew'

from websites.models import Website


def std_contextual_data(request, site=None, site_handle=''):
    site = site or Website.objects.get(handle=site_handle)
    site.link_with_site_handle = site_handle != ''

    ct = {
        'user': request.user,
        'path': request.path,
        'site': site
    }
    return ct
