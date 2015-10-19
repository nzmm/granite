from django.contrib import admin
from reversion.admin import VersionAdmin
from assets.forms import PlainTextAssetAdminForm
from assets.models import (
    PlainTextAsset,
    FileAsset,
)


@admin.register(PlainTextAsset)
class PlainTextAssetAdmin(VersionAdmin):
    list_display = ('handle',)
    form = PlainTextAssetAdminForm


@admin.register(FileAsset)
class FileAssetAdmin(admin.ModelAdmin):
    list_display = ('handle', 'url',)
    readonly_fields = ('url',)
