from django.shortcuts import render
from .forms import TutoriaInicialForm, EducationalProgram, emprendimiento, adicciones , EmpleoIngresosForm, vivienda, tiemposTransporte
from .forms import pueblosOriginarios, fpersonal, fdiscapacidad, fneurodiversidad, fsalud, fsaludmental
# Create your views here.

def home(request):
    return render(request, "core/home.html")

def encuesta(request):
    data = {
        #Creacion de instancia de TutoriaInicialForm 
        'form': TutoriaInicialForm()
    }
    if request.method =='POST':
        formulario = TutoriaInicialForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Respuestas Guardadas"
        else:
            data["form"] = formulario
    
    return render(request, "core/encuesta.html", data)

def survey_eduprog(request):
    data = {
        #Creacion de instancia de TutoriaInicialForm 
        'form': EducationalProgram()
    }

    return render(request, "core/survey_eduprog.html", data)

def emprend(request):
    data = {
        'form': emprendimiento()
    }
    return render(request, "core/emprend.html", data)

def adiccion(request):
    data = {
        'form': adicciones()
    }
    return render(request, "core/adicciones.html", data)

def Empleo(request):
    data = {
        'form' : EmpleoIngresosForm()
    }
    return render(request, "core/encuestaEmpleo.html", data)

def vivienda_f(request):
    data = {
        'form': vivienda()
    }
    return render(request, 'core/encuesta_vivienda.html', data)

def tiempos_f(request):
    data = {
        'form': tiemposTransporte()
    }
    return render(request, "core/encuesta_tiempos.html", data)

def pueblos_f(request):
    data = {
        'form' : pueblosOriginarios()
    }
    return render(request, 'core/encuesta_pueblos.html', data)  

def personal_f(request):
    data = {
        'form' : fpersonal()
    }
    return render(request, "core/encuesta_personal.html", data)

def discapacidad_f(request):
    data = {
        'form' : fdiscapacidad()
    }
    return render(request, 'core/encuesta_discapacidad.html', data)

def neurodiversidad_f(request):
    data = {
        'form' : fneurodiversidad()
    }
    return render(request, 'core/encuesta_neuro.html', data)

def salud_f(request):
    data = {
        'form' : fsalud()
    }
    return render(request, 'core/encuesta_salud.html', data)

def saludmental_f(request):
    data = {
        'form' : fsaludmental()
    }
    return render(request, 'core/encuesta_saludm.html', data)