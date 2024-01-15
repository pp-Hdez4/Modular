from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import usuarioForm1, usuarioEstudianteForm1, loginusuarioForm, usuarioTutorForm1
from django.http import HttpRequest
from .models import Usuario, Estudiante
#from .forms import InformacionForm
import re
from datetime import datetime

# Create your views here

def nuevoUsuario(request):
    data = {
        'form' : usuarioForm1()
    }
    patron_alumnos = r'^[a-zA-Z0-9._%+-]+@alumnos\.udg\.mx$'
    patron_academicos = r'^[a-zA-Z0-9._%+-]+@academicos\.udg\.mx$'
    
    if request.method == 'POST':
        regex = re.compile(patron_alumnos) #verificar si correo es de alumnos
        regex2 = re.compile(patron_academicos) #verificar si correo es de academicos

        if regex.match(request.POST.get('correo')):

            formulario = usuarioForm1(request.POST)
            if formulario.is_valid():

                dato = formulario.cleaned_data
                dato['rol'] = 1
                objeto = Usuario.objects.create(**dato)

                request.session['codigo_udg'] = objeto.codigo_udg
                request.session['nombre'] = objeto.nombre

                return redirect('perfilestudiante')
                #data['mensaje'] = "Correo valido alumnos"

        elif regex2.match(request.POST.get('correo')): #verificar si es correo de academicos 
            #data['mensaje'] = "Correo valido academicos"
            datos_user = {
                'correo' : request.POST.get('correo'),
                'password' : request.POST.get('password'),
                'activo' : True,
                'rol' : 2, #tutor
                'perfil' : False,
            }

        else:
            data['mensaje'] = "Correo no valido"

    return render(request, 'accounts/register.html', data)


def estudianteView(request):
    
    usuario_id = request.session.get('codigo_udg', None)
    nombre = request.session.get('nombre', None)
    data = {
        #'form' : usuarioEstudianteForm1(initial={'nombre': datos_temporales.get('codigo_udg', '')})
        'form' : usuarioEstudianteForm1(),
        'usuario_id' : usuario_id,
        'nombre' : nombre,
    }

    if request.method == 'POST':
        formulario = usuarioEstudianteForm1(request.POST)
        if formulario.is_valid():
            dato = formulario.cleaned_data
            dato['codigo_udg_id'] = usuario_id

            datoCarrera = formulario.cleaned_data['career']
            carrera_id = datoCarrera.id
            data['career_id'] = carrera_id

            modelo_user = Usuario.objects.get(pk=usuario_id)  # Ajusta esto según tu relación
            modelo_user.perfil = True
            modelo_user.save()




            Estudiante.objects.create(**dato)

            #data['mensaje'] = "Guardado"

        return redirect('home_student')
    
    return render(request, 'accounts/registerE1.html', data)

def home_student(request):
    nombre = request.session.get('nombre', None)
    data = {
        'nombre' : nombre,
    }
    return render(request, 'accounts/prueba.html', data)


def tutorView(request):
    data = {
        'form' : usuarioTutorForm1()
    }
    return render(request, 'accounts/registerT1.html', data)

def login_userV(request):

    data = {
        'form' : loginusuarioForm()
    }
    return render(request, 'accounts/login.html', data)


