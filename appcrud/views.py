from django.shortcuts import render
from datetime import date
from .models import Persona
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm

# Create your views here.
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
            return redirect(to="personas")

    datos={
        "form":form
    }
    return render(request,'appcrud/crearpersona.html', datos)
