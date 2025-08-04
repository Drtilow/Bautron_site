from django import forms
from .models import Poptavka

class PoptavkaForm(forms.ModelForm):
    class Meta:
        model = Poptavka
        fields = ['jmeno', 'email', 'telefon', 'popis']
