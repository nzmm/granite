"""granite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from pages.views import (
    retrieve_with_handle,
    retrieve_with_host
)

urlpatterns = [
    url(r'^(?P<site_handle>\w+)/$', retrieve_with_handle),
    url(r'^(?P<site_handle>\w+)/pages/', retrieve_with_handle),
    url(r'^$', retrieve_with_host),
    url(r'^pages/', retrieve_with_host),
]
