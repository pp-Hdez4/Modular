from django.shortcuts import render



from .forms import   crearSesionForm

# Create your views here.

#solucion rama daniel
"""def solicitarAsesoriaView(request):
    data = {
        'form' : solicitarAsesoriaForm()
    }
    return render(request, 'globalcore/asesorianueva.html', data)"""




def crearSesionView(request):
    data = {
        'form' : crearSesionForm()
    }
    return render(request, 'globalcore/crearSesion.html', data)