from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10,primary_key=True, null=False)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50, null=False)
    fecha_ncto=models.DateField(verbose_name='Fecha de Nacimiento',error_messages='ta malo')
    correo=models.EmailField(error_messages='coloca bien el correo...')
    telefono=models.IntegerField()

    def __str__(self):
        return f"RUT:{self.rut} NOMBRE: {self.nombre} {self.apellido}"
    
class Mascota(models.Model):
    nombre=models.CharField(max_length=100, null=False)
    tipo=models.CharField(max_length=50)
    propietario=models.ForeignKey(Persona,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre