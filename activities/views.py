from django.shortcuts import render
from .forms import InicioActividad1Form

# Create your views here.
def InicioActividad1v(request):
    data = {
        #Creacion de instancia de TutoriaInicialForm 
        'form': InicioActividad1Form()
    }
    if request.method =='POST':
        #es un update al formulario con id referenciado a la tutoria
        formulario = InicioActividad1Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Respuestas Guardadas"
        else:
            data["form"] = formulario
    
    return render(request, "activities/actividad1d1.html", data)
