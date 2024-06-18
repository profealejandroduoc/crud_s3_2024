from django.db import models
from .enumeraciones import *
from django.contrib.auth.models import User 

# Create your models here.

class Perfil(models.Model):
    usuario=models.OneToOneField(User,related_name='usuario', on_delete=models.CASCADE)
    telefono=models.CharField(max_length=9, null=False)
    direccion=models.CharField(max_length=250,null=False)

class Persona(models.Model):
    rut=models.CharField(max_length=10,primary_key=True, null=False)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50, null=False)
    fecha_ncto=models.DateField(verbose_name='Fecha de Nacimiento',error_messages='ta malo')
    correo=models.EmailField(error_messages='coloca bien el correo...')
    telefono=models.IntegerField()
    imagen=models.ImageField(upload_to='personas',null=True)

    def __str__(self):
        return f"RUT:{self.rut} NOMBRE: {self.nombre} {self.apellido}"
    
class Mascota(models.Model):
    nombre=models.CharField(max_length=100, null=False)
    tipo=models.CharField(max_length=50,choices=TIPO_MASCOTA,default="OTRO")
    pais=models.CharField(max_length=50, choices= sorted(CODIGO_PAIS, key=lambda x: x[1]),default="Sin asignar")
    propietario=models.ForeignKey(Persona,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.PROTECT)
    persona=models.ForeignKey(Persona, on_delete=models.PROTECT)
    cantidad=models.IntegerField()