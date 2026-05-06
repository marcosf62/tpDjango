from django import forms

from .models import Prof

class InfoProf(forms.ModelForm):
    class Meta:
        model = Prof
        fields = [

            "nombre",
            "descripcion",

        ]