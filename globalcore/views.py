from django.shortcuts import render
from .forms import  crearReporteForm
# Create your views here.

#solucion rama daniel
"""def solicitarAsesoriaView(request):
    data = {
        'form' : solicitarAsesoriaForm()
    }
    return render(request, 'globalcore/asesorianueva.html', data)"""

def crearReporteView(request):
    data = {
        'form' : crearReporteForm()
    }
    return render(request, 'globalcore/crearReporte.html', data)


