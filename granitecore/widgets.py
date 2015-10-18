__author__ = 'matthew'

from django.forms.widgets import Widget
from django.utils.encoding import force_text
from django.forms.utils import flatatt
from django.utils.html import format_html


TEMPLATE_EDITOR_HTML = """
<br><br>
<textarea{} style="display:none;" readonly>{}</textarea>
<div style="float:right;position:relative;top:-24px;height:0;margin-bottom:8px;">
    <label for="mode-sel"><strong>Content type:</strong></label>
    <select id="mode-sel">
        <option value="html">HTML</option>
        <option value="css">CSS</option>
        <option value="javascript">Javascript</option>
    </select>
</div>
<div id="g-template-editor" style="border-radius:2px;border:2px solid #aaa;width:100%;min-height:450px;">{}</div>
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
        return format_html(TEMPLATE_EDITOR_HTML, flatatt(final_attrs), force_text(value), force_text(value), final_attrs['id'])
