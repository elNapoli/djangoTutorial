from django.conf.urls import url, include
from apps.adopciones.views import SolicitudList, SolicitudCreate
app_name = 'adopciones'
urlpatterns = [
    url(r'^solicitud/listar/', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nuevo/', SolicitudCreate.as_view(), name='solicitud_crear'),
]
