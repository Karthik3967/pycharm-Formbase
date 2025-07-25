from django import forms
from .models import Visitor


class visitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name','message']
