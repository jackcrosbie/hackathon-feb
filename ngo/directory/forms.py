from django import forms
from .models import OrgDirectory, Event


class ProductForm(forms.ModelForm):
    class Meta:
        model = OrgDirectory
        fields = 'location'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'location': 'Location',
        }
