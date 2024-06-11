from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    
    rut=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese rut sin puntos y con guión ej.:12345678-9"}, 
                        help_text="Debe ingresar rut")
    
    fecha_ncto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Persona
        fields = ['rut','imagen','nombre', 'apellido','fecha_ncto', 'correo','telefono']

class UpdatePersonaForm(forms.ModelForm):
    
    rut=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese rut sin puntos y con guión ej.:12345678-9"}, 
                        help_text="Debe ingresar rut")
    
    fecha_ncto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Persona
        fields = ['imagen','nombre', 'apellido','fecha_ncto', 'correo','telefono']