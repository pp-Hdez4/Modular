"""
URL configuration for Modular project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from accounts import views as vaccount 
from accounts.views import CustomLoginView
from adminprofile import views as vadmin
from globalcore import views as vglobal
from chatbot import views as vchat
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),

    path('encuesta/', views.encuesta, name="encuesta"),
    path('survey_eduprog/', views.survey_eduprog, name = "survey_eduprog"),
    path('admin/', admin.site.urls),
    path('emprend/', views.emprend, name = "emprend"),
    path('adicciones/', views.adiccion, name = "adicciones"),
    path('encuesta_empleo/', views.Empleo, name="Empleo"),
    path('encuesta_vivienda/', views.vivienda_f, name = "vivienda"),
    path('encuesta_tiempos/', views.tiempos_f, name = "tiempos_transporte"),
    path('encuesta_pueblos/', views.pueblos_f, name = "pueblos_originarios"),
    path('encuesta_personal/', views.personal_f, name = "personal"),
    path('encuesta_discapacidad/', views.discapacidad_f, name = "discapacidad"),
    path('encuesta_neurodiversidad/', views.neurodiversidad_f, name = "neurodiversidad"),
    path('encuesta_salud/', views.salud_f, name = "salud"),
    path('encuesta_saludm/', views.saludmental_f, name = "salud_mental"),
    path('encuesta_tics/', views.tics_f, name = "tics"),
    
    

    #accounts

    path('register/', vaccount.registerUser, name='register'),
    path('perfil1/', vaccount.registerStudent, name = 'Perfil1'),
    path('perfil1/verificacion/', vaccount.VerificarEstudiante, name = 'Verificar1'),
    path('perfil2/', vaccount.registerTutor, name = 'Perfil2'),
    path('perfil2/verificacion/', vaccount.VerificarTutor, name = 'Verificar2'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('solicitar_asesoria/', vaccount.solicitarAsesoria_View, name="solicitar_asesoria"),
    path('mostrar_asesorias/', vaccount.mostrarAsesorias, name="mostrar_asesorias" ),
    path('actualizar-asesoria/<int:asesoria_id>/', vaccount.actualizar_asesoria, name='actualizar_asesoria'),
    path('reporteasesoria/', vaccount.crearReporteView, name= "reporteasesoria"),

    
    
    

    #admin profile
    path('coordinacion/', vadmin.coordinacionView, name = 'nuevacoordinacion' ),

    #path('asesorianueva', vglobal.solicitarAsesoriaView, name = 'asesorianueva' ),#


    path('sesion/', vglobal.crearSesionView, name = 'nuevaSesion'),


    
    
    
    #chatbot
    path('chat/', vchat.ChatPage , name= "chatbot"),
    path('getResponse', vchat.getResponse, name= "getResponse"),
    
]
