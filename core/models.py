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
    
    def __str__(self):
        return self.Nombres