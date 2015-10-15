from django.contrib import admin
from .models import (
    PlainTextAsset,
    FileAsset,
    Template,
    Page,
    Website,
)


@admin.register(PlainTextAsset)
class PlainTextAssetAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FileAsset)
class FileAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'handle', 'role')


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name',)
