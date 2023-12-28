from django import forms
from .models import TutoriaIngreso

class TutoriaInicialForm(forms.ModelForm):
    class Meta:
        model = TutoriaIngreso
        #Incluir todos los atributos en el orden del modelo
        fields = '__all__'
        widgets = {
            'ApellidoPaterno': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 150px;'}),
            'ApellidoMaterno': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 150px;'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 150px;'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 150px;'}),
            'Municipio': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 150px;'}),
            'FechaNacimiento': forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
            'pregunta_radio': forms.RadioSelect(),
            # Agrega más campos según sea necesario
        }
        #Incluir los atributos de uno en uno del modelo
        #fields = ["CodigoEstudiante", "ApellidoPaterno", "ApellidoMaterno", "Nombres", "Telefono", "Genero", "ProgramaEducativo", "Municipio", "FechaNacimiento", "EstadoCivil", "importancia"]
        
        
        