from django.shortcuts import render
from .forms import solicitarAsesoriaForm
# Create your views here.


def solicitarAsesoriaView(request):
    data = {
        'form' : solicitarAsesoriaForm()
    }
    return render(request, 'globalcore/asesorianueva.html', data)