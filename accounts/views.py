from django.shortcuts import render, redirect
from .forms import usuarioForm1, usuarioEstudianteForm1, loginusuarioForm, usuarioTutorForm1
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
        #formulario = usuarioForm1(request.POST)

        regex = re.compile(patron_alumnos) #verificar si correo es de alumnos
        regex2 = re.compile(patron_academicos) #verificar si correo es de academicos

        if regex.match(request.POST.get('correo')):

            #formulario = usuarioForm1(request.POST)

            fecha = datetime.now().strftime("%d/%m/%Y")
            datos_user = {
                'codigo_udg' : request.POST.get('codigo_udg'),
                'correo' : request.POST.get('correo'),
                'password': request.POST.get('password'),
                'activo' : True,
                'fecha_registro' : fecha,
                'rol' : 1, #estudiante
                'perfil' : False,
            }
            #data['mensaje'] = "Correo valido alumnos"
            #if formulario.is_valid():
            #formulario.save()

        elif regex2.match(request.POST.get('correo')): #verificar si es correo de academicos 
            #data['mensaje'] = "Correo valido academicos"
            datos_user = {
                'codigo_udg' : request.POST.get('codigo_udg'),
                'correo' : request.POST.get('correo'),
                'password' : request.POST.get('password'),
                'activo' : True,
                'fecha_registro' : fecha,
                'rol' : 2, #tutor
                'perfil' : False,
            }

        else:
            data['mensaje'] = "Correo no valido"

    return render(request, 'accounts/register.html', data)


def estudianteView(request):
    data = {
        #'form' : usuarioEstudianteForm1(initial={'nombre': datos_temporales.get('codigo_udg', '')})
        'form' : usuarioEstudianteForm1()
    }

    #if request.method == 'POST':

        #second_form = usuarioEstudianteForm1(request.POST)

        #datos_student = second_form.cleaned_data

        #return redirect('signup_student2')

    return render(request, 'accounts/registerE1.html', data)

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


