
#from django.forms import ModelForm
#from django import forms
#from .models import reporte

"""class solicitarAsesoriaForm(ModelForm):
    class Meta:
        model = asesoria
        fields = ['calendario', 'motivo']"""
        
        
        

from django.forms import ModelForm
from django import forms
from .models import reporte, sesion
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone
from datetime import timedelta, datetime
from django.forms.widgets import SelectDateWidget




class CustomSelectDateWidget(SelectDateWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener la fecha de mañana y la fecha 15 días después
        tomorrow = datetime.now() + timedelta(days=1)
        max_date = tomorrow + timedelta(days=15)
        
        # Configurar los límites del widget
        self.years = range(tomorrow.year, max_date.year + 1)
        self.months = {i: i for i in range(1, 13)}
        self.days = {i: i for i in range(1, 32)}

class crearSesionForm(ModelForm):
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        min_date = timezone.now() + timedelta(days=1)
        max_date = timezone.now() + timedelta(days=16)

        if fecha < min_date.date():
            raise forms.ValidationError("La fecha debe ser a partir de mañana.")
        elif fecha > max_date.date():
            raise forms.ValidationError("La fecha no puede ser más de 15 días en el futuro.")
        
        return fecha
    
    def clean_hora(self):
        hora = self.cleaned_data['hora']
        min_hora = timezone.datetime.combine(timezone.now(), timezone.datetime.min.time()) + timedelta(hours=9)
        max_hora = timezone.datetime.combine(timezone.now(), timezone.datetime.min.time()) + timedelta(hours=19)

        if hora < min_hora.time():
            raise forms.ValidationError("El horario mínimo es a las 9:00 am.")
        elif hora > max_hora.time():
            raise forms.ValidationError("El horario máximo es a las 7:00 pm.")
        
        return hora

    
    class Meta:
        model = sesion
        fields = ['titulo', 'fecha', 'modalidad', 'sitio', 'hora']
        widgets = {
            'titulo' : forms.TextInput(attrs={ 'placeholder': 'Titulo de la sesion', 'type': 'text'}),
            'fecha' : CustomSelectDateWidget,
           # 'fecha' : forms.SelectDateWidget(years = range(1953, 2006)),
            'hora' : forms.TimeInput(attrs={'type': 'time'}),
            'sitio' : forms.TextInput(attrs={ 'placeholder': 'Ingrese el sitio ya sea aula, cubículo o enlace de sesion', 'type': 'text'}),
        }
        #fecha = forms.DateField(widget=CustomSelectDateWidget)
        labels = {
            'sitio' : 'Ingrese el sitio de reunion',
        }
