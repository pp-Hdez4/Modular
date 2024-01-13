from django.forms import ModelForm
from django import forms
from .models import asesoria

class solicitarAsesoriaForm(ModelForm):
    class Meta:
        model = asesoria
        fields = ['calendario', 'motivo']
        

