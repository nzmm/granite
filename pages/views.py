from django.shortcuts import render
from pages.models import Page
from granite.utils.views import std_contextual_data


def retriever(request, site_handle):
    path = request.path.split(site_handle, 1)[-1]
    data = std_contextual_data(request, site_handle)

    if path == '/':
        pages = Page.objects.filter(site__handle=site_handle, role=Page.HOME, published=True)
    else:
        pages = Page.objects.filter(site__handle=site_handle, handle=path, published=True)
    if not pages:
        return render(request, 'nopages.html', data)

    page = pages.first()
    data.update({'page': page})

    return render(request, page.template.template_path, data)
