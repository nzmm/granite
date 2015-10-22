__author__ = 'matthew'

from websites.models import Website


def std_contextual_data(request, site=None, site_handle=''):
    ct = {
        'user': request.user,
        'path': request.path,
        'site': site or Website.objects.get(handle=site_handle)
    }
    return ct
