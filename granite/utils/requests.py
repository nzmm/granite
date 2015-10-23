__author__ = 'Matthew'

from websites.models import Website


def get_host_matcher(request):
    return request.get_host().split('.', 1)[-1]


def site_from_host(request):
    host_match = get_host_matcher(request)
    try:
        site = Website.objects.get(hosts__contains=host_match)
    except Website.DoesNotExist:
        return None
    except Website.MultipleObjectsReturned:
        print(Website.objects.filter(hosts__contains=host_match))
    return site


def page_within_scope(request, handle):
    site = site_from_host(request)
    if site is None:
        if request.user.is_active:
            return True
        return False
    elif site.handle == handle:
        return True
    return False

