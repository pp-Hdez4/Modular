
from django.forms import ModelForm
from .models import usuario, estudiante
from django import forms


class usuarioForm1(ModelForm):
    class Meta:
        model = usuario
        fields = ['codigo_udg', 'correo']

class usuarioEstudianteForm1(ModelForm):
    class Meta:
        model = estudiante
        fields = ['nombre', 'apellido_m', 'apellido_p', 'carrera', 'fecha_nacimiento', 'telefono', 'estadocivil', 'sexo', 'municipio']
        widgets = {
            'estadocivil': forms.RadioSelect(),
            'sexo' : forms.RadioSelect(),
            'fecha_nacimiento' : forms.SelectDateWidget(years = range(1953, 2006))
        }

class usuarioEstudianteForm2(ModelForm):
    class Meta:
        model = usuario
        fields = ['password']


class loginusuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['codigo_udg', 'password']
        widgets = {
            'codigo_udg': forms.TextInput(attrs={ 'placeholder': 'Codigo Universidad de Guadalajara'}),
            'password' : forms.TextInput(attrs={ 'placeholder': 'Contraseña', 'type': 'password'}),
        }
        labels = {
        'codigo_udg': '',
        'password' : '',
        # Puedes personalizar otras etiquetas aquí
        }


