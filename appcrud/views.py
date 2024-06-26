from django.shortcuts import render
from datetime import date
from .models import Persona
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm, UpdatePersonaForm
from django.contrib import messages
from os import path, remove
from django.conf import settings

# Create your views here.
#def login(request):
#   return render(request, 'appcrud/login.html')


def index(request):
    return render(request, 'appcrud/index.html')

def personas(request):
    hoy=date.today()
 
    
    personas=Persona.objects.all()

    datos={
        "fecha":hoy,
        
        "personas":personas
    }

    return render(request,'appcrud/personas.html', datos)

def detallepersona(request,id):
     #persona=Persona.objects.get(rut=id)
     persona=get_object_or_404(Persona, rut=id)
     datos={
         "persona":persona
     }
     return render(request,'appcrud/detallepersona.html', datos)



def crearpersona(request):
    
    form=PersonaForm()

    if request.method=="POST":
        form=PersonaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona agregada al registro')
            return redirect(to="personas")

    datos={
        "form":form
    }
    return render(request,'appcrud/crearpersona.html', datos)

def modificarpersona(request, id):
    persona=get_object_or_404(Persona,rut=id)

    form=UpdatePersonaForm(instance=persona)
    datos={
        "form":form,
        "persona":persona
    }

    if request.method=="POST":
        form=UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            messages.warning(request,'Persona Modificada')
            return redirect(to='personas')
        
    return render(request,'appcrud/modificarpersona.html',datos)

def eliminarpersona(request, id):
    persona=get_object_or_404(Persona,rut=id)

    datos={
        "persona":persona
    }

    if request.method=="POST":
        if persona.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+persona.imagen.url))
        persona.delete()
        messages.error(request, 'Persona Eliminada')
        return redirect(to='personas')
 
        
    return render(request,'appcrud/eliminarpersona.html',datos)
