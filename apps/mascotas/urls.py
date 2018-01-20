from django.conf.urls import url, include
from apps.mascotas.views import index
urlpatterns = [
    url(r'^index/', index),
]
