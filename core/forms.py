from django import forms
from .models import TutoriaIngreso, EducationalProgram, emprendimiento, adicciones , EmpleoIngresos

#Formulario de tutoria de ingreso encuesta.html
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
            'Recomendacion':  forms.RadioSelect(attrs={'class': 'text-primary','style': 'background-color: #fff;'}),
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

class emprendimiento(forms.ModelForm):
    class Meta:
        model = emprendimiento
        fields = '__all__'
        widgets = {     
            'is_emprendimiento': forms.RadioSelect(),
            'is_interesting' : forms.RadioSelect(),
            'if_option' : forms.RadioSelect(),
            'tools_udg' : forms.RadioSelect(),
            'is_community' : forms.RadioSelect(),
        }

class adicciones(forms.ModelForm):
    class Meta:
        model = adicciones
        fields = '__all__'
        widgets = {
            'smoke' : forms.RadioSelect(),
            'w_smoke' : forms.RadioSelect(),
            't_smoke' : forms.RadioSelect(),
            'drinks_alcohol' : forms.RadioSelect(),
            'other_smoke' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            't_alcohol' : forms.RadioSelect(),
        }
        
class EmpleoIngresosForm(forms.ModelForm):
    class Meta:
        
        model = EmpleoIngresos
        fields = '__all__'
        widgets = {
            'TrabajoActual' : forms.RadioSelect(),
            'TrabajoRelacionadoCarrera' : forms.RadioSelect(),
            'HorasTrabajadasSemana' : forms.RadioSelect(),
            'IngresoMensualTrabajo' : forms.RadioSelect(),
            'AportacionEconomicaImportancia' : forms.RadioSelect(),
               
        }    

class vivienda(forms.ModelForm):
    class Meta:
        model = e_vivienda
        fields = '__all__'
        widgets = {
            'responsable_ecnm': forms.RadioSelect(),
            'viveAct': forms.RadioSelect(),
            'otro_vive' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'apoyo_economico': forms.RadioSelect(),
            'is_foraneo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
        }

class tiemposTransporte(forms.ModelForm):
    class Meta:
        model = e_tiemposTrs
        fields = '__all__'
        widgets = {
            'medio_trns': forms.RadioSelect(),
            'otro_trns' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'timetransport' : forms.RadioSelect(),
        }

        # Personaliza el init para excluir campos específicos
        #Incluir los atributos de uno en uno del modelo
        #fields = ["CodigoEstudiante", "ApellidoPaterno", "ApellidoMaterno", "Nombres", "Telefono", "Genero", "ProgramaEducativo", "Municipio", "FechaNacimiento", "EstadoCivil", "importancia"]
        
        
        