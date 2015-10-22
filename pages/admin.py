from django.contrib import admin
from django.contrib.auth.models import User
from reversion.admin import VersionAdmin
from pages.models import (
    Template,
    Page,
)
from pages.forms import (
    TemplateAdminForm,
    PageAdminForm
)


@admin.register(Template)
class TemplateAdmin(VersionAdmin):
    list_display = ('handle', 'site', 'template_path')
    list_filter = ('site__name',)
    readonly_fields = ('template_path',)
    form = TemplateAdminForm


@admin.register(Page)
class PageAdmin(VersionAdmin):
    list_display = ('title', 'site', 'handle', 'role', 'description')
    list_filter = ('site__name',)
    ordering = ('site', 'role', 'title')
    form = PageAdminForm

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'page_author':
            kwargs["initial"] = request.user
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super(PageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
