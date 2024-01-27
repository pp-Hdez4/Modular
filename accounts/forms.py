
from django.forms import ModelForm
from .models import Usuario, Estudiante, Tutor, ProgramaEducativo, PerfilEstudiante, PerfilTutor
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # Puedes personalizar el formulario aquí si es necesario
    # Por defecto, AuthenticationForm ya incluye los campos de nombre de usuario y contraseña
    # Pero puedes añadir más campos si lo necesitas
    # También puedes personalizar las etiquetas, widgets, etc.
    class Meta:
        model = User
        fields = ['username', 'password']
        
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

class usuarioForm1(ModelForm):
    class Meta:
        model = Usuario
        fields = ['codigo_udg', 'nombre','apellido_m', 'apellido_p','correo', 'password', 'sexo', 'fecha_nacimiento']
        widgets = {
            'codigo_udg': forms.TextInput(attrs={ 'placeholder': 'Codigo Univerisidad'}),
            'nombre' : forms.TextInput(attrs={ 'placeholder': 'Nombre'}),
            'apellido_m' : forms.TextInput(attrs={ 'placeholder': 'Apellido Materno'}),
            'apellido_p': forms.TextInput(attrs={ 'placeholder': 'apellido Paterno'}),
            'correo' : forms.TextInput(attrs={ 'placeholder': 'Correo Institucional'}),
            'password' : forms.TextInput(attrs={ 'placeholder': 'Password', 'type': 'password'}),
            'fecha_nacimiento' : forms.SelectDateWidget(years = range(1953, 2006)),
        }
        labels = {
        'codigo_udg' : '',
        'nombre' : '',
        'apellido_m' : '',
        'apellido_p' : '',
        'correo' : '',
        'password' : '',
        'sexo' : 'Selecciona tu sexo :',
        # Puedes personalizar otras etiquetas aquí
        }
        
class usuarioEstudianteForm1(ModelForm):
    class Meta:
        model = Estudiante
        
        fields = ['career', 'ciclo_admision', 'ciclo_actual', 'telefono', 'residencia', 'estado_civil']
        widgets = {
            'ciclo_actual' : forms.TextInput(attrs={ 'placeholder': 'Ciclo Actual Ejemplo: 20B'}),
            'telefono' : forms.TextInput(attrs={ 'placeholder': 'Telefono'}),
            'residencia' : forms.TextInput(attrs={ 'placeholder': 'Municipio de Residencia'}),
            'estado_civil': forms.RadioSelect(),
        }
        labels = {
            'career': 'Selecciona tu programa educativo',
            'estado_civil' : 'Seleccione su estado civil: ',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Personaliza el campo 'autor' para cargar opciones desde la tabla de autores
            self.fields['career'].queryset = ProgramaEducativo.objects.all()

class usuarioTutorForm1(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'

class loginusuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'password']
        widgets = {
            'correo': forms.TextInput(attrs={ 'placeholder': 'Correo Institucional'}),
            'password' : forms.TextInput(attrs={ 'placeholder': 'Contraseña', 'type': 'password'}),
        }
        labels = {
        'codigo_udg': '',
        'password' : '',
        # Puedes personalizar otras etiquetas aquí
        }
