
from django.forms import ModelForm
from .models import coordinacion
from django import forms



class coordinacionForm(ModelForm):
    class Meta:
        model = coordinacion
        fields = '__all__'