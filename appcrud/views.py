from django.shortcuts import render
from datetime import date
from .models import Persona

# Create your views here.
def index(request):
    return render(request, 'appcrud/index.html')

def personas(request):
    hoy=date.today()
    print("Fecha de hoy",hoy)
    saludo="Hola desde una vista"
    personas=Persona.objects.all()

    datos={
        "fecha":hoy,
        "saludo":saludo,
        "personas":personas
    }

    return render(request,'appcrud/personas.html', datos)