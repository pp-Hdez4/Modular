
from django.forms import ModelForm
from .models import ProgramaEducativo, PerfilEstudiante, PerfilTutor, Asesoria
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#autenticate django users
class LoginForm(AuthenticationForm):
    # Puedes personalizar el formulario aquí si es necesario
    # Por defecto, AuthenticationForm ya incluye los campos de nombre de usuario y contraseña
    # Pero puedes añadir más campos si lo necesitas
    # También puedes personalizar las etiquetas, widgets, etc.
    class Meta:
        model = User
        fields = ['username', 'password']
        

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        labels = {
            'password1' : '',
            'password2' : '',
            'username' : 'Codigo Universidad de Guadalajara',
            'first_name' : 'Nombre',
            'last_name' : 'Apellidos',
            'email' : '',
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Para quitar la propiedad help_text de un campo específico
            self.fields['username'].help_text = ''      
        
#registro de usuarios
class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password' : forms.TextInput(attrs={ 'placeholder': 'Password', 'type': 'password'}),
            'username' : forms.TextInput(attrs={ 'placeholder': 'Codigo Universidad de Guadalajara'}),
            'first_name' : forms.TextInput(attrs={ 'placeholder': 'Nombre'}),
            'last_name' : forms.TextInput(attrs={ 'placeholder': 'Apellidos'}),
            'email' : forms.TextInput(attrs={ 'placeholder': 'Correo', 'type' : 'email'}),
        }
        labels = {
            'password' : '',
            'username' : '',
            'first_name' : '',
            'last_name' : '',
            'email' : '',
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Para quitar la propiedad help_text de un campo específico
            self.fields['username'].help_text = ''    

class PerfilEstudianteForm(ModelForm):
    class Meta:
        model = PerfilEstudiante
        fields = ['carrera', 'sexo', 'fecha_nacimiento', 'telefono', 'estado_civil', 'ciclo_admision', 'ciclo_actual']
        widgets = {
            'telefono' : forms.TextInput(attrs={ 'placeholder': 'Ingresa tu numero telefonico'}),
            'ciclo_admision' : forms.TextInput(attrs={ 'placeholder': 'Ejemplo 22A'}),
            'ciclo_actual' : forms.TextInput(attrs={ 'placeholder': 'Ejemplo 22 A'}),
            'fecha_nacimiento' : forms.SelectDateWidget(years = range(1953, 2006)),
        }
        labels = {
            'carrera' : 'Selecciona tu carrera',
            'sexo' : 'Elige tu sexo',
            'fecha_nacimiento' : 'Selecciona dia, mes y año correspondiente a tu fecha de nacimiento',
        }

class PerfilTutorForm(ModelForm):
    class Meta:
        model = PerfilTutor
        fields = ['sexo', 'fecha_nacimiento', 'depto']
        widgets = {
            'fecha_nacimiento' : forms.SelectDateWidget(years = range(1953, 2006)),
        }

class VerificacionEstudianteForm(ModelForm):
    class Meta:
        model = PerfilEstudiante
        fields = [
            'codigo_verificar'
        ]
        widgets = {
            'codigo_verificar' : forms.TextInput(attrs={ 'placeholder': 'Codigo de Verificacion'})
        }
        labels = {
            'codigo_verificar' : '',
        }

class VerificacionTutorForm(ModelForm):
    class Meta:
        model = PerfilTutor
        fields = [
            'codigo_verificar'
        ]
        widgets = {
            'codigo_verificar' : forms.TextInput(attrs={ 'placeholder': 'Codigo de Verificacion'})
        }
        labels = {
            'codigo_verificar' : '', 
        }
        
#Registro asesoria
class solicitarAsesoriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = [ 'motivos', 'tipo' ]
        widgets = {
            'motivos' : forms.TextInput(attrs={ 'placeholder': 'Ingresa los motivos para solicitar la tutoria'})
        }
        
        
