__author__ = 'matthew'

from django.forms.widgets import Widget
from django.utils.encoding import force_text
from django.forms.utils import flatatt
from django.utils.html import format_html


EDITOR_HTML = """
<br><br><textarea{} style="display:none;" readonly>{}</textarea><div id="g-template-editor" style="border-radius:2px;border:2px solid #aaa;width:100%;min-height:600px;">{}</div>
"""


class TemplateEditor(Widget):

    def __init__(self, attrs=None):
        default_attrs = {}
        if attrs:
            default_attrs.update(attrs)
        super(TemplateEditor, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return format_html(EDITOR_HTML, flatatt(final_attrs), force_text(value), force_text(value), final_attrs['id'])
