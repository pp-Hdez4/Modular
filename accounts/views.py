from django.shortcuts import render, redirect
from .forms import usuarioForm1, usuarioEstudianteForm1, usuarioEstudianteForm2
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
                'activo' : True,
                'fecha_registro' : fecha,
                'rol' : 1, #estudiante
            }
            #data['mensaje'] = "Correo valido alumnos"

            request.session['datos_temporales'] = datos_user

            return redirect('signup_estudent')

            #if formulario.is_valid():
            #formulario.save()

        elif regex2.match(request.POST.get('correo')): #verificar si es correo de academicos 
            #data['mensaje'] = "Correo valido academicos"
            datos_user = {
                'codigo_udg' : request.POST.get('codigo_udg'),
                'correo' : request.POST.get('correo'),
                'activo' : True,
                'fecha_registro' : fecha,
                'rol' : 2, #tutor
            }

        else:
            data['mensaje'] = "Correo no valido"

    return render(request, 'accounts/register.html', data)


def estudianteView(request):

    datos_temporales1 = request.session.get('datos_temporales', {})

    data = {
        #'form' : usuarioEstudianteForm1(initial={'nombre': datos_temporales.get('codigo_udg', '')})
        'form' : usuarioEstudianteForm1()
    }

    if request.method == 'POST':

        #second_form = usuarioEstudianteForm1(request.POST)

        #datos_student = second_form.cleaned_data

        datos_student = {
            'nombre' : request.POST.get('nombre'),
        }

        request.session['datos_temporales2'] = datos_student

        return redirect('signup_student2')
        

    return render(request, 'accounts/registerE1.html', data)


def passwordViewEstudiante(request):

    datos_temporales1 = request.session.get('datos_temporales', {})
    datos_temporales2 = request.session.get('datos_temporales2', {})

    data = {
        'form' : usuarioEstudianteForm2()
    }

    #if request.method == 'POST':

    data['mensaje'] = datos_temporales1.get('codigo_udg', '') + datos_temporales2.get('nombre', '')

    return render(request, 'accounts/registerE2.html', data)
