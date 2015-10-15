from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import (
    PlainTextAsset,
    FileAsset,
    Template,
    Page,
    Website,
)


@admin.register(PlainTextAsset)
class PlainTextAssetAdmin(VersionAdmin):
    list_display = ('handle',)


@admin.register(FileAsset)
class FileAssetAdmin(admin.ModelAdmin):
    list_display = ('handle', 'file')


@admin.register(Template)
class TemplateAdmin(VersionAdmin):
    pass


@admin.register(Page)
class PageAdmin(VersionAdmin):
    list_display = ('title', 'handle', 'role')


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name',)
