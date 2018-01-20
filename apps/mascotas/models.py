from django.db import models
from apps.adopciones.models import Personas

# Create your models here.


class Vacunas(models.Model):
    nombre = models.CharField(max_length=50)

class Mascotas(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacunas)