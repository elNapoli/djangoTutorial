from django.contrib.auth.models import User
from apps.usuarios.forms import UsuarioRegistroForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuarios/registrar.html'
    form_class = UsuarioRegistroForm
    success_url = reverse_lazy('mascotas:mascota_listar')


