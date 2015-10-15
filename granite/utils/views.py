__author__ = 'matthew'


def std_contextual_data(request):
    ct = {
        'user': request.user,
        'path': request.path,
    }
    return ct
