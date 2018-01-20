from django.db import models

# Create your models here.

class Personas(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
    persona = models.ForeignKey(Personas, null=True, blank=True,on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()