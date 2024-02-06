from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser
# Create your models here.

roles = [
    [1, "Estudiante"],
    [2, "Tutor"]
]

OpcionesEstadoCivil = [
    [1 ,"Soltero/Soltera"],
    [2,"Matrimonio"],
    [3,"Union Libre"],
    [4,"Viudez"]
]

OpcionesGenero = [
    [1,"Hombre"],
    [2,"Mujer"],
    [3,"Prefiero no decirlo"],
    [4,"No binario"]
]

opciones_carreras = [
    ['LFI', 'Licenciatura en Fisica'],
    ['LMT', 'Licenciatura en Matematicas'],
    ['INNI', 'Ingenieria en Informatica'],
    ['INCO', 'Ingenieria en Computacion'],
    ['QFB', 'Quimico Farmaceutico Biólogo']
]

opcionesCalendario = [
    ('18B', '2018B'),
    ('19A', '2019A'),
    ('19B', '2019B'),
]

calendarioActual = [
    ('24A', '2024B')
]

deptos = [
    ('INNI', 'Informatica'),
]

# Opciones para la pregunta con radio buttons
OpcionesMaterias = [
    ('Programacion', "Programacion"),
    ('Calculo', "Calculo"),
    ('Pre calculo', "Pre calculo"),
    ('Fisica', "Fisica"),
    ('Algoritmia', "Algoritmia"),
]

class ProgramaEducativo(models.Model):
    #id automatico
    nombre = models.CharField("Nombre: ", max_length = 100)
    correo = models.CharField("Nombre: ", max_length = 100)

    def __str__(self):
        return self.nombre

class Division(models.Model):
    #id automatico
    nombre = models.CharField("Nombre: ", max_length = 100)

class PerfilEstudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #llave de usuario foranea
    codigo_verificar = models.CharField(max_length = 10) #codigo de verificacion
    carrera = models.CharField(choices = opciones_carreras, default = 1, max_length = 100) #carrera de estudiante
    sexo = models.IntegerField(choices = OpcionesGenero, default = 1) #sexo
    fecha_nacimiento = models.DateField() #fecha de nacimiento
    asesorado = models.BooleanField(default = False) #status del asesorado
    telefono = models.CharField("",max_length = 10) #numero telefonico
    estado_civil = models.IntegerField(choices = OpcionesEstadoCivil, default = 1) #estado civil
    residencia = models.CharField("",max_length = 150) #lugar de residencia
    ciclo_admision = models.CharField(choices = opcionesCalendario,max_length = 3, default='18B')
    ciclo_actual = models.CharField("",max_length = 3, default = '', blank = False)

class PerfilTutor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #llave de usuario foranea
    codigo_verificar = models.CharField(max_length = 10) #codigo de verificacion
    sexo = models.IntegerField(choices = OpcionesGenero, default = 1) #sexo
    fecha_nacimiento = models.DateField() #fecha de nacimiento
    depto = models.CharField(choices = deptos, default = 1, max_length = 100)

opcionesAsesoria = [
    ('Inicio', "Inicio"),
    ('Trayecto', "Trayecto"),
    ('Egreso', "Egreso"),
]

opcionesStatus = [
    ('Aceptada', 'Aceptada'),
    ('Cancelada', 'Cancelada'),
]

class Asesoria(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asesorias_alumno')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asesorias_tutor')
    motivos = models.CharField(max_length=150)
    tipo = models.CharField(max_length = 20, choices = opcionesAsesoria, default = 'Inicio')
    status = models.CharField(max_length = 20, choices = opcionesAsesoria, default = 'Solicitada')
    #materia = models.CharField(choices=OpcionesMaterias, max_length = 30)


