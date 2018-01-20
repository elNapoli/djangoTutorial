from django.urls import path
from apps.mascotas.views import index
urlpatterns = [
    path('', index),
]
