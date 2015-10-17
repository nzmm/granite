__author__ = 'matthew'

from granitecore.models import Website


def std_contextual_data(request, site_handle):
    ct = {
        'user': request.user,
        'path': request.path,
        'site': Website.objects.get(handle=site_handle)
    }
    return ct
