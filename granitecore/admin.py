from django.contrib import admin
from .models import (
    Asset,
    Template,
    Page,
    Website,
)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name',)
