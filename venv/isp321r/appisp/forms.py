from appisp.models import *
from django import forms
from django.core.exceptions import ValidationError

class AddNewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('name', 'date', 'img', 'info')