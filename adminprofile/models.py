from django.db import models

# Create your models here.

class coordinacion(models.Model):
    #id automatico
    nombre = models.CharField("Nombre: ", max_length = 100)
    correo =  models.CharField("Correo: ", max_length = 100)
    coordinador = models.CharField("Coordinador: ", max_length = 120)




