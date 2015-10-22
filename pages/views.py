from django.shortcuts import render
from pages.models import Page
from granite.utils.requests import site_from_host
from granite.utils.views import std_contextual_data


def retrieve_with_handle(request, site_handle):
    path = request.path.split(site_handle, 1)[-1]
    data = std_contextual_data(request, site_handle=site_handle)
    site = site_from_host(request)
    print(site.handle, site_handle)

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
    site = site_from_host(request)
    data = std_contextual_data(request, site)

    if request.path == '/':
        pages = Page.objects.filter(site=site, role=Page.HOME, published=True)
    else:
        pages = Page.objects.filter(site=site, handle=request.path, published=True)
    if not pages:
        return render(request, 'nopages.html', data)

    page = pages.first()
    data.update({'page': page})

    return render(request, page.template.template_path, data)
