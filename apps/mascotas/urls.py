from django.conf.urls import url, include
from apps.mascotas.views import index, mascota_view
app_name = 'mascotas'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/', mascota_view, name='mascota_crear'),
]
