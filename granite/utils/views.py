__author__ = 'matthew'

from granite.utils.requests import get_host_matcher
from websites.models import Website


def std_contextual_data(request, site=None, site_handle=''):
    print(request.get_host(), request.path)
    site = site or Website.objects.get(handle=site_handle)
    site.link_with_site_handle = get_host_matcher(request) in site.hosts

    ct = {
        'user': request.user,
        'path': request.path,
        'site': site
    }
    return ct
