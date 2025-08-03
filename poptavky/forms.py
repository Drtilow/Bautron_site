from django import forms
from .models import Poptavka

# Formulář pro vytvoření nové poptávky
class PoptavkaForm(forms.ModelForm):
    class Meta:
        model = Poptavka
        fields = ['jmeno', 'email', 'telefon', 'popis']
        widgets = {
            'popis': forms.Textarea(attrs={'rows': 4}),
        }
