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
    mascotas = Mascotas.objects.all().order_by('id')
    contexto = {'mascotas': mascotas}
    return render(request,'mascotas/mascotas_list.html',contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascotas.objects.get(id = id_mascota)
    if request.method == 'GET':
        form = MascotasForm(instance=mascota)
    else:
        form = MascotasForm(request.POST, instance= mascota)
        if form.is_valid():
            form.save()
        return redirect('mascotas:mascota_listar')
    return render(request, 'mascotas/mascotas_form.html',{'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascotas.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas:mascota_listar')
    return render(request, 'mascotas/mascota_delete.html', {'mascota': mascota})


