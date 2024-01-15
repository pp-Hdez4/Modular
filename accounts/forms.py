
from django.forms import ModelForm
from .models import Usuario, Estudiante, Tutor, ProgramaEducativo
from django import forms

#registro de usuarios
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

            primer_autor = ProgramaEducativo.objects.first()
            if primer_autor:
                self.fields['career'].widget.choices = [(primer_autor.id, primer_autor)] + list(self.fields['career'].widget.choices)[1:]

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
