#from django.forms import ModelForm
#from django import forms
#from .models import reporte

"""class solicitarAsesoriaForm(ModelForm):
    class Meta:
        model = asesoria
        fields = ['calendario', 'motivo']"""
        


<<<<<<< HEAD
from django.forms import ModelForm
from django import forms
from .models import  sesion
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone
from datetime import timedelta, datetime
from django.forms.widgets import SelectDateWidget




class CustomSelectDateWidget(SelectDateWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

=======
>>>>>>> parent of 183e20d (Merge branch 'master' into Rama-Pepe)
        

