from django import forms
from apps.adopciones.models import Personas,Solicitud

class PersonasForm(forms.ModelForm):

    class Meta:
        model = Personas

        fields =[
            'nombre',
            'apellidos',
            'edad',
            'email',
            'domicilio',
        ]

        labels ={
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'email': 'Correo',
            'domicilio': 'Domicilio',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),

        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud

        fields = [
            'numero_mascotas',
            'razones',
        ]

        labels = {
            'numero_mascotas': 'Nro de mascotas',
            'razones': 'Razones para adoptar',

        }

        widgets = {
            'numero_mascotas': forms.TextInput(attrs={'class': 'form-control'}),
            'razones': forms.TextInput(attrs={'class': 'form-control'}),

        }