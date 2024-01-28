from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegisterForm, PerfilEstudianteForm, PerfilTutorForm, VerificacionEstudianteForm, VerificacionTutorForm,LoginForm
from django.http import HttpRequest
from .models import PerfilEstudiante, PerfilTutor
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
#from .forms import InformacionForm
import re
from datetime import datetime
from .forms import UserRegisterForm
import random
import string
#login
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        # Autenticar al usuario
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                # Obtener todos los grupos del usuario
                user_groups = user.groups.all()
                if user_groups.exists():
                    # Si el usuario pertenece a algún grupo, redirigir a la página del grupo
                    group_name = user_groups[0].name  # Obtener el nombre del primer grupo al que pertenece
                    if group_name == 'Estudiantes':
                        return HttpResponseRedirect(reverse('home'))
                    elif group_name == 'Tutores':
                        return HttpResponseRedirect(reverse('home'))
                    # Añadir más condiciones para otros grupos si es necesario
                else:
                    # Si el usuario no pertenece a ningún grupo, redirigir a la página principal
                    return HttpResponseRedirect(reverse('login'))
        return super().form_invalid(form)

def registerUser(request):

    patron_alumnos = r'^[a-zA-Z0-9._%+-]+@alumnos\.udg\.mx$'
    patron_academicos = r'^[a-zA-Z0-9._%+-]+@academicos\.udg\.mx$'

    data = {
        'form' : UserRegistrationForm()
    }

    if request.method == 'POST':

        regex = re.compile(patron_alumnos) #verificar si correo es de alumnos
        regex2 = re.compile(patron_academicos) #verificar si correo es de academicos

        if regex.match(request.POST.get('email')): #alumnos email
            form = UserRegistrationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():
                #dato = form.cleaned_data
                #dato['is_active'] = 0
                email = form.cleaned_data['email']
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                #objeto = User.objects.create(**dato) #auth_user
                user_id = user.id
                request.session['id'] = user_id
                request.session['nombre'] = user.first_name
                #request.session['id'] = objeto.id
                #request.session['nombre'] = objeto.first_name
                request.session['correo'] = email

                #grupo_estudiantes = Group.objects.get(name='Estudiantes')
                #grupo_estudiantes.user_set.add(objeto)

                group_name = 'Estudiantes'  # Reemplaza 'Nombre_del_Grupo' con el nombre del grupo al que quieres asignar el usuario
                group = Group.objects.get(name=group_name)
                group.user_set.add(user)

                return redirect('Perfil1')
            
        elif regex2.match(request.POST.get('email')): #profesores email 

            form = UserRegistrationForm(request.POST)
            if form.is_valid():

                email = form.cleaned_data['email']
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                user_id = user.id
                request.session['id'] = user_id
                request.session['nombre'] = user.first_name
                request.session['correo'] = email
                
                group_name = 'Tutores'
                group = Group.objects.get(name=group_name)
                group.user_set.add(user)

                return redirect('Perfil2')
                #return redirect('PerfilTutor')
        else:
            data['mensaje'] = "Correo no valido, debe ser institucional"

            #return redirect('login_user') Puedes cambiar esto a la página a la que quieras redirigir después del registro
    else:
        data = {
        'form' : UserRegistrationForm()
        #'form' : UserRegisterForm()
    }
    return render(request, 'registration/register.html', data)

def cadena_aleatoria(longitud):
    caracteres = string.ascii_letters + string.digits
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud))
    return cadena_aleatoria

def registerStudent(request):
    usuario_id = request.session.get('id', None)
    nombre = request.session.get('nombre', None)
    correo = request.session.get('correo', None)

    data = {
        'form' : PerfilEstudianteForm(),
        'usuario_id' : usuario_id,
        'nombre' : nombre,
    }

    if request.method == 'POST':
        form = PerfilEstudianteForm(request.POST)
        if form.is_valid():
            dato = form.cleaned_data
            usuario = User.objects.get(id=usuario_id) #auth_user
            dato['usuario'] = usuario
            cadena = cadena_aleatoria(8)
            dato['codigo_verificar'] = cadena

            objeto = PerfilEstudiante.objects.create(**dato)
            request.session['id_profile'] = objeto.id #perfil
            send_mail(
                    'Bienvenida a nuestro sitio',
                    'Ingresa el siguiente codigo para comenzar en la plataforma: ' + cadena,
                    'acciontutorial.cucei@gmail.com', # Remitente
                    [correo], # Lista de destinatarios
                    fail_silently=False,
                )
            return redirect('Verificar1')
            #generar codigo aleatorio y enviar por correo registrado anteriormente
    
    return render(request, 'registration/profilestudent.html', data)

def registerTutor(request):
    usuario_id = request.session.get('id', None)
    nombre = request.session.get('nombre', None)
    correo = request.session.get('correo', None)

    data = {
        'form' : PerfilTutorForm(),
        'usuario_id' : usuario_id,
        'nombre' : nombre,
    }

    if request.method == 'POST':
        form = PerfilTutorForm(request.POST)
        if form.is_valid():
            dato = form.cleaned_data
            usuario = User.objects.get(id=usuario_id)
            dato['usuario'] = usuario
            cadena = cadena_aleatoria(8)
            dato['codigo_verificar'] = cadena

            objeto = PerfilTutor.objects.create(**dato)
            request.session['id_profile'] = objeto.id #perfil
            send_mail(
                    'Bienvenida a nuestro sitio',
                    'Ingresa el siguiente codigo para comenzar en la plataforma: ' + cadena,
                    'acciontutorial.cucei@gmail.com', # Remitente
                    [correo], # Lista de destinatarios
                    fail_silently=False,
                )
            return redirect('Verificar2')
            #generar codigo aleatorio y enviar por correo registrado anteriormente
    
    return render(request, 'registration/profiletutor.html', data)

def VerificarEstudiante(request):
    data = {
        'form' : VerificacionEstudianteForm()
    }
    usuario_id = request.session.get('id', None)
    nombre = request.session.get('nombre', None)
    correo = request.session.get('correo', None)
    perfil_id = request.session.get('id_profile', None)

    if request.method == 'POST':
        form = VerificacionEstudianteForm(request.POST)
        if form.is_valid():
            dato = form.cleaned_data
            perfil = PerfilEstudiante.objects.get(id=perfil_id)
            if perfil.codigo_verificar == dato['codigo_verificar']:
                #activar el perfil
                usuario = User.objects.get(id=usuario_id)
                usuario.is_active = True
                usuario.save()
                request.session.clear()
                return redirect('login')
            else:
                data['mensaje'] = 'El codigo no coincide, intenta de nuevo'

    return render(request, 'registration/verificacion.html', data)

def VerificarTutor(request):
    data = {
        'form' : VerificacionTutorForm()
    }
    usuario_id = request.session.get('id', None)
    nombre = request.session.get('nombre', None)
    correo = request.session.get('correo', None)
    perfil_id = request.session.get('id_profile', None)

    if request.method == 'POST':
        form = VerificacionEstudianteForm(request.POST)
        if form.is_valid():
            dato = form.cleaned_data
            perfil = PerfilTutor.objects.get(id=perfil_id)
            if perfil.codigo_verificar == dato['codigo_verificar']:
                #activar el perfil
                usuario = User.objects.get(id=usuario_id)
                usuario.is_active = True
                usuario.save()
                request.session.clear()
                return redirect('login')
            else:
                data['mensaje'] = 'El codigo no coincide, intenta de nuevo'

    return render(request, 'registration/verificaciont.html', data)

