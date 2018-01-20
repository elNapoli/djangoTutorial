from django.urls import path
from apps.adopciones.views import index
urlpatterns = [
    path('', index),
]
