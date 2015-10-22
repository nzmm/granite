from django.shortcuts import render
from pages.models import Page
from websites.models import Website
from granite.utils.views import std_contextual_data


def retrieve_with_handle(request, site_handle):
    path = request.path.split(site_handle, 1)[-1]
    data = std_contextual_data(request, site_handle=site_handle)

    if path == '/':
        pages = Page.objects.filter(site__handle=site_handle, role=Page.HOME, published=True)
    else:
        pages = Page.objects.filter(site__handle=site_handle, handle=path, published=True)
    if not pages:
        return render(request, 'nopages.html', data)

    page = pages.first()
    data.update({'page': page})

    return render(request, page.template.template_path, data)


def retrieve_with_host(request):
    host_match = request.get_host().split('.', 1)[-1]
    site = Website.objects.get(hosts__contains=host_match)
    data = std_contextual_data(request, site)

    if request.path == '/':
        pages = Page.objects.filter(site__handle=site_handle, role=Page.HOME, published=True)
    else:
        pages = Page.objects.filter(site__handle=site_handle, handle=path, published=True)
    if not pages:
        return render(request, 'nopages.html', data)

    page = pages.first()
    data.update({'page': page})

    return render(request, page.template.template_path, data)
