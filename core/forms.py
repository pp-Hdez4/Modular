from django import forms
from .models import TutoriaIngreso, EducationalProgram, emprendimiento, adicciones , EmpleoIngresos, e_vivienda, e_tiemposTrs, mpueblos_orig, mpersonal, mdiscapacidad, mneurodiversidad, msalud, msaludmental, maccesotics


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
            'is_foraneo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;', 'placeholder': 'Tu respuesta'}),
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

class pueblosOriginarios(forms.ModelForm):
    class Meta:
        model = mpueblos_orig
        fields = '__all__'
        widgets = {
            'comunidad': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'lengua': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
        }

class fpersonal(forms.ModelForm):
    class Meta:
        model = mpersonal
        fields = '__all__'
        widgets = {
            'comunidadlgbt': forms.RadioSelect(),
            'identidadGen': forms.RadioSelect(),
            'other_identidad': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'hijos' : forms.RadioSelect(),
            'hijoscuidado': forms.RadioSelect(),
            'avanzcuidado': forms.RadioSelect(),
        }

class fdiscapacidad(forms.ModelForm):
    class Meta:
        model = mdiscapacidad
        fields = '__all__'
        widgets = {
            'es_discapacidad' : forms.RadioSelect(),
            'tipod' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;', 'placeholder': 'Tu respuesta'}),
            'dispositivo_d' : forms.RadioSelect(),
            'tiposdispositivod' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
        }

class fneurodiversidad(forms.ModelForm):
    class Meta:
        model = mneurodiversidad
        fields = '__all__'
        widgets = {
            'tipoNeurodiversidad' : forms.RadioSelect(),
            'otrotipo_neuro' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'diagnostico' : forms.RadioSelect(),
            'tratamiento' : forms.RadioSelect(),
            
        }

class fsalud(forms.ModelForm):
    class Meta:
        model = msalud
        fields = '__all__'
        widgets = {
            'tiposangre' : forms.RadioSelect(),
            'otro_sangre' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'enfermedad_salud' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'alergias' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
        }

class fsaludmental(forms.ModelForm):
    class Meta:
        model = msaludmental
        fields = '__all__'
        widgets = {
            'suenio' : forms.RadioSelect(),
            'cansancio' : forms.RadioSelect(),
            'fobias' : forms.RadioSelect(),
            'irritacion' : forms.RadioSelect(),
            'ansiedad'  : forms.RadioSelect(),
            'motivacion' : forms.RadioSelect(),
            'pensamientos' : forms.RadioSelect(),
            'tristeza' : forms.RadioSelect(),
            'felicidad' : forms.RadioSelect(),
            'terapia' : forms.RadioSelect(),
        }

class ftics(forms.ModelForm):
    class Meta:
        model = maccesotics
        fields = '__all__'
        widgets = {
            'internet' : forms.RadioSelect(),
            'lugar_estudio' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'horas' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'nmaterias' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'horasclases' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'horaslibres' :forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'perfil' : forms.RadioSelect(),
            'malla' : forms.RadioSelect(),
            'materias_pre' : forms.RadioSelect(),
        }


        # Personaliza el init para excluir campos específicos
        #Incluir los atributos de uno en uno del modelo
        #fields = ["CodigoEstudiante", "ApellidoPaterno", "ApellidoMaterno", "Nombres", "Telefono", "Genero", "ProgramaEducativo", "Municipio", "FechaNacimiento", "EstadoCivil", "importancia"]
        
        
        