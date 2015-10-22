__author__ = 'Matthew'

from websites.models import Website


def site_from_host(request):
    host_match = request.get_host().split('.', 1)[-1]
    try:
        site = Website.objects.get(hosts__contains=host_match)
    except Website.DoesNotExist:
        return ''
    return site
