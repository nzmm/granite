__author__ = 'Matthew'

from django.forms import ModelForm
from pages.models import Template, Page
from granite.widgets import TextEditor, ContentEditor


class TemplateAdminForm(ModelForm):
    class Meta:
        model = Template
        fields = ('site', 'handle', 'markup')
        widgets = {
          'markup': TextEditor(),
        }


class PageAdminForm(ModelForm):
    class Meta:
        model = Page
        fields = (
            'site',
            'title',
            'handle',
            'page_description',
            'content',
            'template',
            'role',
            'page_author',
            'published'
        )
        widgets = {
          'content': ContentEditor(),
        }
