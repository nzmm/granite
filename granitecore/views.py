from django.shortcuts import render
from granitecore.models import Page
from django.db.models import Q


def home_page_handler(request):
    print(request.path)
    pages = Page.objects.filter(Q(handle='/') | Q(role='home'))
    if not pages:
        return render(request, 'nopages.html', {})

    page = pages.first()
    return render(request, page.template.path, {'content': page.content, 'path': request.path})


def url_handler(request):
    pages = Page.objects.filter(handle=request.path)
    if not pages:
        return render(request, 'nopages.html', {})

    page = pages.first()
    return render(request, page.template.path, {'content': page.content, 'path': request.path})
