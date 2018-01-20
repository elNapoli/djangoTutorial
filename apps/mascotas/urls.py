from django.conf.urls import url, include
from apps.mascotas.views import index, mascota_view, mascotas_list
app_name = 'mascotas'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/', mascota_view, name='mascota_crear'),
    url(r'^listar/', mascotas_list, name='mascota_listar'),
]
