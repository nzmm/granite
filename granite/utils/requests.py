__author__ = 'Matthew'

import tldextract
from websites.models import Website


def get_host_matcher(request):
    ext = tldextract.extract(request.get_host())
    return ext.registered_domain


def site_from_host(request):
    host_match = get_host_matcher(request)
    try:
        site = Website.objects.get(hosts__contains=host_match)
    except Website.DoesNotExist:
        print(request.get_host(), host_match, Website.objects.filter(hosts__contains=host_match))
        return None
    except Website.MultipleObjectsReturned:
        print(request.get_host(), host_match, Website.objects.filter(hosts__contains=host_match))
        return None
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

