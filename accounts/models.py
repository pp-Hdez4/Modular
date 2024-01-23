from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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

class ProgramaEducativo(models.Model):
    #id automatico
    nombre = models.CharField("Nombre: ", max_length = 100)
    correo = models.CharField("Nombre: ", max_length = 100)

    def __str__(self):
        return self.nombre

class Division(models.Model):
    #id automatico
    nombre = models.CharField("Nombre: ", max_length = 100)

class Usuario(models.Model):
    
    codigo_udg = models.CharField(max_length = 10, primary_key = True)
    correo = models.CharField(max_length = 100)
    password = models.CharField(max_length = 10)
    rol = models.IntegerField()

    nombre = models.CharField("", max_length = 100)
    apellido_m = models.CharField("", max_length = 100)
    apellido_p = models.CharField("", max_length = 100)

    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default = True)
    fecha_registro = models.DateField(auto_now_add=True)
    perfil = models.BooleanField(default = False)
    sexo = models.IntegerField(choices = OpcionesGenero, default = 1)

    def save(self, *args, **kwargs):
        # Asigna la fecha actual al campo fecha_registro al guardar el objeto
        self.fecha_registro = datetime.today().date()
        super().save(*args, **kwargs)

class Estudiante(models.Model):
    #id automatico
    codigo_udg = models.ForeignKey(Usuario, on_delete = models.CASCADE) #llave foranea
    career =  models.ForeignKey(ProgramaEducativo, on_delete=models.CASCADE, default = 1)
    #datos escolares
    ciclo_admision = models.CharField(choices = opcionesCalendario,max_length = 3, default='18B')
    ciclo_actual = models.CharField("",max_length = 3, default = '', blank = False)
    #datos personales
    telefono = models.CharField("",max_length = 10)
    asesorado = models.BooleanField(default = False)
    residencia = models.CharField("",max_length = 150)
    estado_civil = models.IntegerField(choices = OpcionesEstadoCivil, default = 1)

class Tutor(models.Model):
    #id automatico
    #llave foranea
    codigo_udg = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    #datos tutor especiales
    alumnos_n = models.IntegerField()
    division_id = models.ForeignKey(Division, on_delete=models.CASCADE)





