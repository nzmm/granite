from django.db import models
from django.contrib import admin
from reversion.admin import VersionAdmin
from granite.widgets import TextEditor
from assets.models import (
    PlainTextAsset,
    FileAsset,
)


@admin.register(PlainTextAsset)
class PlainTextAssetAdmin(VersionAdmin):
    list_display = ('handle',)
    formfield_overrides = {
        models.TextField: {'widget': TextEditor},
    }


@admin.register(FileAsset)
class FileAssetAdmin(admin.ModelAdmin):
    list_display = ('handle', 'url', 'thumbnail_small')
    readonly_fields = ('url', 'thumbnail_large',)
