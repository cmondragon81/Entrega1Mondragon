from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    clave=models.CharField(max_length=12)
    materia=models.CharField(max_length=30)
    turno_manana=models.BooleanField()
    turno_tarde=models.BooleanField()
    turno_noche=models.BooleanField()


    def __str__(self):
        return f'{self.nombre}'