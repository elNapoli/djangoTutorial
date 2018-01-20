from django import forms
from apps.mascotas.models import Mascotas
class MascotasForm(forms.ModelForm):

    class Meta:
        model = Mascotas

        fields =[

            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        labels ={
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),

        }