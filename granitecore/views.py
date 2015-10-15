from django.shortcuts import render
from granitecore.models import Page
from django.db.models import Q
from granite.utils.views import std_contextual_data


def url_handler(request):
    data = std_contextual_data(request)

    if request.path == '/':
        pages = Page.objects.filter(Q(handle='/') | Q(role=Page.HOME))
    else:
        pages = Page.objects.filter(handle=request.path)
    if not pages:
        return render(request, 'nopages.html', data)

    page = pages.first()
    data.update({'page': page})

    return render(request, page.template.path, data)
