from django.db import models
from django import forms

# Create your models here.
OpcionesGenero = [
    [0,"Hombre"],
    [1,"Mujer"],
    [2,"Prefiero no decirlo"],
    [3,"No binario"]
]

OpcionesProgramaEducativo = [
    [0,"Ingenieria en Computacion"],
    [1,"Ingenieria en Informatica"]
]

OpcionesEstadoCivil = [
    [0 ,"Soltero/Soltera"],
    [1,"Matrimonio"],
    [2,"Union Libre"],
    [3,"Viudez"]
]

OpcionesImportancia = [
    [1, "1 - Muy Bajo"],
    [2, "2 - Bajo"],
    [3, "3 - Moderado"],
    [4, "4 - Alto"],
    [5, "5 - Muy Alto"],
]

# Opciones para la pregunta con radio buttons
OpcionesPregunta = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]

rankingOptions = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
]



class TutoriaIngreso(models.Model):
    CodigoEstudiante = models.IntegerField()
    ApellidoPaterno = models.CharField(max_length=150)
    ApellidoMaterno = models.CharField(max_length=150)
    Nombres = models.CharField(max_length=150)
    Telefono = models.IntegerField()
    Genero = models.IntegerField(choices=OpcionesGenero)
    ProgramaEducativo = models.IntegerField(choices=OpcionesProgramaEducativo)
    Municipio = models.CharField(max_length=150)
    FechaNacimiento = models.DateField()
    EstadoCivil = models.IntegerField(choices= OpcionesEstadoCivil)
    importancia = models.IntegerField(choices=OpcionesImportancia)
    pregunta_radio = models.IntegerField(choices=OpcionesPregunta, default=1)
    
    ActividadCine = models.BooleanField("Cine", default=False)
    ActividadMuseos = models.BooleanField("Museos", default=False)
    ActividadConciertos = models.BooleanField("Conciertos", default=False)
    ActividadLeerLibros = models.BooleanField("Leer Libros", default=False)
    ActividadFeriasCulturales = models.BooleanField("Ferias culturales", default=False)
    ActividadDeporte = models.BooleanField("Deporte", default=False)
    ActividadOtro = models.CharField(max_length=150,default='')
    
    
    def __str__(self):
        return self.Nombres

class EducationalProgram(models.Model):
    #meanings
    Recomendacion = models.IntegerField(choices = rankingOptions, default=1)
    Plan_de_Estudios = models.IntegerField(choices = rankingOptions, default=1) #plan de estudios
    Planta_Academica = models.IntegerField(choices = rankingOptions, default=1) #planta academica
    Instalaciones = models.IntegerField(choices = rankingOptions, default=1) #instalaciones
    Costos = models.IntegerField(choices = rankingOptions, default=1) #costos
    Horarios = models.IntegerField(choices = rankingOptions, default=1) #horarios
    #motivation
    Prestigio_Institucion = models.IntegerField(choices = rankingOptions, default=1) #prestigio
    Reconocimiento_social_familiar = models.IntegerField(choices = rankingOptions, default=1) #reconocimiento
    Superacion_personal = models.IntegerField(choices = rankingOptions, default=1) #superacion
    Actualizacion_campo_laboral = models.IntegerField(choices = rankingOptions, default=1) #actualizacion de campo
    Movilidad_laboral_e_ingresos = models.IntegerField(choices = rankingOptions, default=1) #movilidad laboral/ingresos
    Empresas_solicitan_grado_academico = models.IntegerField(choices = rankingOptions, default=1) #solicitud empresas
    #cultural activities

    cinema = models.BooleanField("Cine", default = False)
    museum = models.BooleanField("Museos", default = False)
    concerts = models.BooleanField("Conciertos", default = False)
    reading = models.BooleanField("Leer libros", default = False)
    cultural_fairs = models.BooleanField("Ferias Culturales", default = False)
    sports = models.BooleanField("Deportes", default = False)
    others = models.CharField(max_length = 150, default = '')


