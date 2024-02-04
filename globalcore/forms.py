from django.forms import ModelForm
from django import forms
from .models import reporte, sesion
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone
from datetime import timedelta, datetime
from django.forms.widgets import SelectDateWidget

class crearReporteForm(ModelForm):
    class Meta:
        model = reporte
        fields = ['titulo', 'situacion']


