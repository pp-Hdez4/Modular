from django.db import models

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



class usuario(models.Model):
    #id automatico
    codigo_udg = models.CharField(max_length = 10)
    correo = models.CharField(max_length = 100)
    password = models.CharField(max_length = 10)
    rol = models.IntegerField()
    activo = models.BooleanField()
    fecha_registro = models.CharField(max_length = 8)

class estudiante(models.Model):
    #id automatico
    nombre = models.CharField("Nombre: ", max_length = 100)
    apellido_m = models.CharField("Apellido Materno", max_length = 100)
    apellido_p = models.CharField("Apellido Paterno", max_length = 100)

    carrera = models.CharField("Selecciona carrera: ",max_length = 100, choices = opciones_carreras, default = 'LFI')

    #fecha de nacimiento
    dia = models.CharField(max_length = 2)
    mes = models.CharField(max_length = 2)
    anio = models.CharField(max_length = 2, verbose_name = "Año")

    fecha_nacimiento = models.DateField()

    #contacto
    telefono = models.CharField(max_length = 10)

    estadocivil = models.IntegerField(choices = OpcionesEstadoCivil, default = 1)
    sexo = models.IntegerField(choices = OpcionesGenero, default = 1)
    municipio = models.CharField(max_length = 100)


