from django.forms import ModelForm
from django import forms
from .models import reporte

"""class solicitarAsesoriaForm(ModelForm):
    class Meta:
        model = asesoria
        fields = ['calendario', 'motivo']"""
        
class crearReporteForm(ModelForm):
    class Meta:
        model = reporte
        fields = ['titulo', 'situacion']
        

