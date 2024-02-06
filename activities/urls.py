from django.urls import path
from . import views

urlpatterns = [
    path('actividad1de1/', views.InicioActividad1v, name='actividad1de1'),
    #path('actividad2de1/', views.InicioActividad2v, name = 'actividad2de1'),
    #path('actividad3de1/', views.InicioActividad3v, name = 'actividad3de1'),
    #Otras URLs de la otra aplicación
]