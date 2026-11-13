from django import forms

from .models import Livre


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ["titre", "auteur", "categorie", "disponible"]
        widgets = {
            "titre": forms.TextInput(attrs={"class": "form-control"}),
            "auteur": forms.TextInput(attrs={"class": "form-control"}),
            "categorie": forms.Select(attrs={"class": "form-select"}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
