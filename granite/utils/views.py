__author__ = 'matthew'

from granitecore.models import Website


def std_contextual_data(request):
    ct = {
        'user': request.user,
        'path': request.path,
        'site': Website.objects.get(pk=1)
    }
    return ct
