from django.db import models

# Create your models here.
"""class asesoria(models.Model):
    #id automatico
    id_estudiante = models.IntegerField()
    id_tutor = models.IntegerField()
    status = models.IntegerField(default = 0)

<<<<<<< HEAD
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
=======
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    
    status = models.IntegerField()
    calendario = models.CharField(max_length = 20)
    motivo = models.TextField()"""
    


>>>>>>> parent of 183e20d (Merge branch 'master' into Rama-Pepe)
