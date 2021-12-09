from django import forms
from .models import *

class AddFileForm(forms.ModelForm):
    class Meta:
        model = SaveFile
        fields = ['title', 'saveFile', 'file_describe']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'file_describe': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
        }


class DelFileForm(forms.ModelForm):
    class Meta:
        model = SaveFile
        fields = []