from django.shortcuts import render,redirect
from apps.mascotas.forms import MascotasForm, Mascotas
# Create your views here.

def index(request):
    return render(request, 'mascotas/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascotas:index')
    else:
        form = MascotasForm()
    return render(request, 'mascotas/mascotas_form.html', {'form': form})

def mascotas_list(request):
    mascotas = Mascotas.objects.all()
    contexto = {'mascotas': mascotas}
    return render(request,'mascotas/mascotas_list.html',contexto)