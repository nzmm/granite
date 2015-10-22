__author__ = 'Matthew'

from websites.models import Website


def site_from_host(request):
    host_match = request.get_host().split('.', 1)[-1]
    try:
        site = Website.objects.get(hosts__contains=host_match)
    except Website.DoesNotExist:
        return None
    return site


def page_within_scope(request, handle):
    site = site_from_host(request)
    if site is None:
        if request.user.is_superuser():
            return True
        return False
    elif site.handle == handle:
        return True
    return False

