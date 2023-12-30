from django import forms
from .models import TutoriaIngreso, EducationalProgram

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
            'ActividadOtro': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 150px;'}),
            
            # Agrega más campos según sea necesario
        }

class EducationalProgram(forms.ModelForm):
    class Meta:
        model = EducationalProgram
        fields = '__all__'
        widgets = {
            'Recomendacion':  forms.RadioSelect(),
            'Plan_de_Estudios': forms.RadioSelect(),
            'Planta_Academica': forms.RadioSelect(),
            'Instalaciones': forms.RadioSelect(),
            'Costos': forms.RadioSelect(),
            'Horarios': forms.RadioSelect(),
            'Prestigio_Institucion': forms.RadioSelect(),
            'Reconocimiento_social_familar': forms.RadioSelect(),
            'Superacion_personal': forms.RadioSelect(),
            'Actualizacion_campo_laboral': forms.RadioSelect(),
            'Movilidad_laboral_e_ingresos': forms.RadioSelect(),
            'Empresas_solicitan_grado_academico': forms.RadioSelect(),
            'others': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 100px;'}),
        }


        # Personaliza el init para excluir campos específicos
        #Incluir los atributos de uno en uno del modelo
        #fields = ["CodigoEstudiante", "ApellidoPaterno", "ApellidoMaterno", "Nombres", "Telefono", "Genero", "ProgramaEducativo", "Municipio", "FechaNacimiento", "EstadoCivil", "importancia"]
        
        
        