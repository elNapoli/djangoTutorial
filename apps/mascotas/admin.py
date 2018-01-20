from django.contrib import admin

# Register your models here.
from apps.mascotas.models import Vacunas,Mascotas

admin.site.register(Vacunas)
admin.site.register(Mascotas)