from django import forms
from .models import TutoriaIngreso

class TutoriaInicialForm(forms.ModelForm):
    class Meta:
        model = TutoriaIngreso
        #Incluir todos los atributos en el orden del modelo
        fields = '__all__'
        #Incluir los atributos de uno en uno del modelo
        #fields = ["CodigoEstudiante", "ApellidoPaterno", "ApellidoMaterno", "Nombres", "Telefono", "Genero", "ProgramaEducativo", "Municipio", "FechaNacimiento", "EstadoCivil", "importancia"]
        
        
        