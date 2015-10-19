__author__ = 'matthew'

from django.forms.widgets import Widget
from django.utils.encoding import force_text
from django.forms.utils import flatatt
from django.utils.html import format_html


class TextEditor(Widget):
    EDITOR_HTML = """
    <br><br>
    <textarea{} style="display:none;" readonly>{}</textarea>
    <div style="float:right;position:relative;top:-24px;height:0;margin-bottom:8px;">
        <label for="mode-sel"><strong>Content type:</strong></label>
        <select id="g-mode-sel">
            <option value="html">HTML</option>
            <option value="css">CSS</option>
            <option value="javascript">Javascript</option>
            <option value="markdown">Markdown</option>
        </select>
    </div>
    <div id="g-editor" style="border-radius:2px;border:2px solid #aaa;width:100%;min-height:450px;">{}</div>
    {% load static from staticfiles %}
    <script src="{% static 'js/ace-min-noconflict/ace.js' %}" type="text/javascript" charset="utf-8"></script>
    <script>
        function splitExt(path) {
            return path.split('.').pop();
        }
        function aceModeFromHandle(editor, handle) {
            var ext = splitExt(handle.value),
                      mode;
            switch(ext) {
                case 'js':
                    mode = 'javascript'
                    break
                case 'css':
                    mode = 'css'
                    break
                case 'md':
                    mode = 'md'
                    break
                case 'htm':
                case 'html':
                default:
                    mode = 'html'
                    break
            }
            if (editor.getSession().getMode() != mode) {
                editor.getSession().setMode("ace/mode/" + mode);
                document.getElementById('g-mode-sel').value = mode;
            }
        }
        (function() {
            var editor = ace.edit("g-editor");
            editor.setFontSize(15);
            editor.setTheme("ace/theme/chrome");
            editor.on("change", function(e) {
                document.querySelector('textarea:read-only').value = editor.getValue();
            });
            // content guesser
            var handle = document.querySelector('input[name="handle"]');
            handle.addEventListener("change", function(e) {
                aceModeFromHandle(editor, handle);
            });
            handle.addEventListener("keyup", function(e) {
                aceModeFromHandle(editor, handle);
            });
            aceModeFromHandle(editor, handle);
            // Ctrl+S
            document.addEventListener("keydown", function(e) {
              if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
                e.preventDefault();
                document.querySelector('input[name="_continue"]').click();
              }
            }, false);
        })();
    </script>
    """

    def __init__(self, attrs=None):
        default_attrs = {}
        if attrs:
            default_attrs.update(attrs)
        super(TextEditor, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return format_html(self.EDITOR_HTML, flatatt(final_attrs), force_text(value), force_text(value), final_attrs['id'])


class ContentEditor(TextEditor):
    EDITOR_HTML = """
    <a href="#" target="_blank" style="float:right;"><strong>View page</strong></a>
    <br>
    <br>
    <textarea{} style="display:none;" readonly>{}</textarea>
    <div class="help" style="width:100%;">Tip: <a href="https://help.github.com/articles/markdown-basics/" target="_blank">Markdown</a> is supported.</div>
    <br>
    <div id="g-editor" style="border-radius:2px;border:2px solid #aaa;width:100%;min-height:400px;">{}</div>
    """

    def __init__(self, attrs=None):
        super(ContentEditor, self).__init__(attrs)
        return
