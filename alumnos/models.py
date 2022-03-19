from django.db import models

# Create your models here.
class alumnos(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    clave=models.CharField(max_length=12)
    email=models.EmailField()
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=50)
    tutor=models.CharField(max_length=50)
    tutor_telefono=models.IntegerField()
    tutor_email=models.EmailField()
    
    