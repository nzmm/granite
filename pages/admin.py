from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from reversion.admin import VersionAdmin
from granite.widgets import TextEditor
from pages.models import (
    Template,
    Page,
)


@admin.register(Template)
class TemplateAdmin(VersionAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TextEditor},
    }


@admin.register(Page)
class PageAdmin(VersionAdmin):
    list_display = ('title', 'site', 'handle', 'role')
    ordering = ('site', 'role', 'title')

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'page_author':
            kwargs["initial"] = request.user
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super(PageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
