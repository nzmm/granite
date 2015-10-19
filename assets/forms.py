__author__ = 'Matthew'

from django.forms import ModelForm
from assets.models import PlainTextAsset
from granite.widgets import TextEditor


class PlainTextAssetAdminForm(ModelForm):
    class Meta:
        model = PlainTextAsset
        fields = ('site', 'handle', 'text')
        widgets = {
          'text': TextEditor(),
        }
