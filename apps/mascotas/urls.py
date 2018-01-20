from django.conf.urls import url, include
from apps.mascotas.views import index, mascota_view, mascotas_list, mascota_edit, mascota_delete
app_name = 'mascotas'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/', mascota_view, name='mascota_crear'),
    url(r'^listar/', mascotas_list, name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/', mascota_delete, name='mascota_eliminar'),
]
