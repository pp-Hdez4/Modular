from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegisterForm, PerfilEstudianteForm, PerfilTutorForm, VerificacionEstudianteForm, VerificacionTutorForm,LoginForm, solicitarAsesoriaForm
from django.http import HttpRequest
from .models import PerfilEstudiante, PerfilTutor, Asesoria , reporte
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
#from .forms import InformacionForm
import re
from datetime import datetime
from .forms import UserRegisterForm , crearReporteForm
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
from .forms import UserRegistrationForm , crearReporteForm
from django.shortcuts import render, redirect, get_object_or_404


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


def solicitarAsesoria_View(request):
    alumno_id = None

    if request.user.is_authenticated:
        alumno_id = request.user.id

    data = {'form': solicitarAsesoriaForm()}

    # Verificar si el estudiante ya tiene una asesoría en curso
    perfil_estudiante = PerfilEstudiante.objects.get(usuario_id=alumno_id)
    if perfil_estudiante.asesorado == 0:  # Verificar si asesorado es 0 (False)
        if request.method == 'POST':
            form = solicitarAsesoriaForm(request.POST)
            if form.is_valid():
                descripcion = form.cleaned_data['motivos']
                materia = form.cleaned_data['tipo']

                tutor = User.objects.get(id=1)

                nueva_asesoria = Asesoria.objects.create(
                    alumno_id=alumno_id,
                    tutor=tutor,
                    descripcion=descripcion,
                    materia=materia
                )
                nueva_asesoria.save()

                # Actualizar el campo 'asesorado' en el perfil del estudiante
                perfil_estudiante.asesorado = True
                perfil_estudiante.save()

                data["mensaje"] = "Asesoría solicitada correctamente."
            else:
                data["form"] = form
    else:
        data['mensaje'] = 'Ya tienes una asesoría en curso.'

    return render(request, 'accounts/asesoria.html', data)





def mostrarAsesorias(request):
    grupo_tutores = Group.objects.get(name='Tutores')
    tutores = grupo_tutores.user_set.all()

    filtro_tutor_id = request.GET.get('filtro_tutor_id')

    if filtro_tutor_id == '1':
        asesorias = Asesoria.objects.filter(tutor_id=1)
    else:
        asesorias = Asesoria.objects.all()

    return render(request, 'accounts/listarAsesorias.html', {'asesorias': asesorias, 'tutores': tutores})

def actualizar_asesoria(request, asesoria_id):
    if request.method == 'POST':
        tutor_id = request.POST.get('TutorID')
        if tutor_id is not None:  # Validar que se haya seleccionado un tutor
            asesoria = get_object_or_404(Asesoria, id=asesoria_id)
            asesoria.tutor_id = tutor_id
            asesoria.save()
    return redirect('mostrar_asesorias')

def crearReporteView(request):
    form = crearReporteForm()
    
    if request.user.is_authenticated:
        alumno_id = request.user.id  # Obtener el ID del estudiante autenticado

        if request.method == 'POST':
            form = crearReporteForm(request.POST)
            if form.is_valid():
                titulo = form.cleaned_data['titulo']
                situacion = form.cleaned_data['situacion']
                
                tutor_id = None
                
                # Consulta la tabla 'accounts_asesoria' filtrando por el ID del estudiante
                asesorias = Asesoria.objects.filter(alumno_id=alumno_id)
                
                # Verifica si hay al menos una asesoría para el estudiante
                if asesorias.exists():
                    # Si hay asesorías, toma el ID del tutor asignado de la primera asesoría encontrada
                    tutor_id = asesorias.first().tutor_id
                else:
                    print("El estudiante no tiene asesorías asignadas")
                
                # Crea el nuevo reporte utilizando el ID del estudiante y el ID del tutor
                nuevo_reporte = reporte.objects.create(id_estudiante_id=alumno_id, id_tutor_id=tutor_id, titulo=titulo, situacion=situacion)
                return redirect('reporteasesoria')
    else:
        form = crearReporteForm()

    data = {
        'form': form
    }
    return render(request, 'accounts/crearReporte.html', data)

