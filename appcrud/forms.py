from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    

    fecha_ncto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Persona
        fields = ['rut','imagen','nombre', 'apellido','fecha_ncto', 'correo','telefono']
