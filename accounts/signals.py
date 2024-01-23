from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


#cuando se recibe el usuario, se asigna a un grupo
#decorador receiver, maneja señales, se ejecuta cuando se emita la señal
#https://www.youtube.com/watch?v=p17T7uZKgFg&list=PLxooeC3-xaNd-ps3l7sttk3pPgn1oYKf2

@receiver(post_save, sender = Profile)
def add__user_to_students_group(sender, instance, created, **kwargs):
    #cuando llegue la señal de guardar un registro, receiver toma el evento y lo manda a esta funcion, agrega al grupo de estudiantes
    if created: 
        try:
            students = Group.objects.get(name = 'estudiante')
            
        except Group.DoesNotExist:
            students = Group.objects.create(name = 'estudiante')
            students = Group.objects.create(name = 'tutor')
            students = Group.objects.create(name = 'administrativo')
            students = Group.objects.create(name = 'coordinador')
        instance.user.groups.add(students)

