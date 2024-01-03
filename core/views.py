from django.shortcuts import render
from .forms import TutoriaInicialForm, EducationalProgram, emprendimiento

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