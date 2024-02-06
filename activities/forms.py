from django import forms
from .models import InicioActividad1

#Formulario de la actividad 1
class InicioActividad1Form(forms.ModelForm):
    class Meta:
        model = InicioActividad1
        fields = '__all__'
        widgets = {
            #Seccion 1
            'Recomendacion':  forms.RadioSelect(attrs={'class': 'text-primary','style': 'background-color: #fff;'}),
            'Plan_de_Estudios': forms.RadioSelect(),
            'Planta_Academica': forms.RadioSelect(),
            'Instalaciones': forms.RadioSelect(),
            'Costos': forms.RadioSelect(),
            'Horarios': forms.RadioSelect(),
            'Prestigio_Institucion': forms.RadioSelect(),
            'Reconocimiento_social': forms.RadioSelect(),
            'Superacion_personal': forms.RadioSelect(),
            'Actualizacion_campo': forms.RadioSelect(),
            'Movilidad_laboral_e_ingresos': forms.RadioSelect(),
            'Empresas_solicitan_grado_academico': forms.RadioSelect(),
            'others_description': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 100px;'}),
            #Seccion2
            'is_emprendimiento': forms.RadioSelect(),
            'is_interesting' : forms.RadioSelect(),
            'if_option' : forms.RadioSelect(),
            'tools_udg' : forms.RadioSelect(),
            'is_community' : forms.RadioSelect(),
            #Seccion 3
            'smoke' : forms.RadioSelect(),
            'w_smoke' : forms.RadioSelect(),
            't_smoke' : forms.RadioSelect(),
            'drinks_alcohol' : forms.RadioSelect(),
            'other_smoke' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            't_alcohol' : forms.RadioSelect(),
            
            #Seccion 4
            'TrabajoActual' : forms.RadioSelect(),
            'TrabajoRelacionadoCarrera' : forms.RadioSelect(),
            'HorasTrabajadasSemana' : forms.RadioSelect(),
            'IngresoMensualTrabajo' : forms.RadioSelect(),
            'AportacionEconomicaImportancia' : forms.RadioSelect(),
            #Seccion 5
            'responsable_ecnm': forms.RadioSelect(),
            'viveAct': forms.RadioSelect(),
            'otro_vive' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'apoyo_economico': forms.RadioSelect(),

            'is_foraneo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),

            'is_foraneo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;', 'placeholder': 'Tu respuesta'}),
            #Seccion 6
            'medio_trns': forms.RadioSelect(),
            'otro_trns' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'timetransport' : forms.RadioSelect(),
            #Seccion 7
            'comunidad': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'lengua': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            #Seccion 8
            'comunidadlgbt': forms.RadioSelect(),
            'identidadGen': forms.RadioSelect(),
            'other_identidad': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'hijos' : forms.RadioSelect(),
            'hijoscuidado': forms.RadioSelect(),
            'avanzcuidado': forms.RadioSelect(),
            #Seccion 9
            'es_discapacidad' : forms.RadioSelect(),
            'tipod' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;', 'placeholder': 'Tu respuesta'}),
            'dispositivo_d' : forms.RadioSelect(),
            'tiposdispositivod' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            #Seccion 10
            'tipoNeurodiversidad' : forms.RadioSelect(),
            'otrotipo_neuro' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'diagnostico' : forms.RadioSelect(),
            'tratamiento' : forms.RadioSelect(),
            #Seccion 11
            'tiposangre' : forms.RadioSelect(),
            'otro_sangre' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'enfermedad_salud' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'alergias' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            #Seccion 12
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
            #Seccion 13
            'internet' : forms.RadioSelect(),
            'lugar_estudio' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'horas' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'nmaterias' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'horasclases' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'horaslibres' :forms.TextInput(attrs={'class': 'form-control form-control-sm', 'style': 'width: 250px;'}),
            'perfil' : forms.RadioSelect(),
            'malla' : forms.RadioSelect(),
            'materias_pre' : forms.RadioSelect(),
            'estilos_aprendizaje' : forms.RadioSelect(),
            
        }
        labels = {
            'others_description' : '',
        }
