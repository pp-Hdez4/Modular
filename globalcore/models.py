from django.db import models
from django.contrib.auth.models import User

status_sesion = [
    ('Open' , 'Abierta'),
    ('Close' , 'Finalizada'),
    ('Canceled' , 'Cancelada'),
]
places = [
    ('PRESENCIAL', 'Presencial'),
    ('VIRTUAL', 'Virtual'),
]

# Create your models here. 
class reporte(models.Model):
    titulo = models.TextField()
    situacion = models.TextField()


class sesion(models.Model):
    user_student =  models.OneToOneField(User, on_delete=models.CASCADE) #llave de usuario foranea
    #user_tutor = models.OneToOneField(User, on_delete=models.CASCADE) #llave de usuario foranea
    titulo = models.CharField("Nombre: ", max_length = 100) #titulo de la asesoria
    fecha = models.DateField() #fecha
    status = models.CharField(choices = status_sesion, default = 1, max_length = 100)
    modalidad = models.CharField(choices = places, max_length = 50)
    comentarios = models.TextField("")
    sitio = models.CharField("", max_length = 150)
    hora = models.TimeField()