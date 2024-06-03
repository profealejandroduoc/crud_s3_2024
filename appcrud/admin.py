from django.contrib import admin
from .models import Persona, Mascota

# Register your models here.

class AdmPersona(admin.ModelAdmin):
    list_display=['rut','nombre', 'apellido','fecha_ncto', 'correo','telefono']
    #list_editable=['nombre', 'apellido','fecha_ncto', 'correo','telefono']
    list_filter=['apellido']


class AdmMascota(admin.ModelAdmin):
    list_display=['id','nombre','tipo','pais','propietario']
    list_editable=['nombre','tipo','pais','propietario']
    list_filter=['propietario','tipo','pais']


admin.site.register(Persona,AdmPersona)
admin.site.register(Mascota,AdmMascota)