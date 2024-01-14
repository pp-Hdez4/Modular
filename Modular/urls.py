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
from adminprofile import views as vadmin
from globalcore import views as vglobal

urlpatterns = [
    #path('', views.home, name="home"),
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
    path('signup/', vaccount.nuevoUsuario , name = 'signup'),
    path('perfilestudiante/', vaccount.estudianteView, name = 'perfilestudiante'),
    path('perfiltutor/', vaccount.tutorView, name = 'perfiltutor'),
    path('login_user/', vaccount.login_userV, name = 'login_user'),

    #admin profile
    path('coordinacion/', vadmin.coordinacionView, name = 'nuevacoordinacion' ),

    #globalcore

    #path('asesorianueva', vglobal.solicitarAsesoriaView, name = 'asesorianueva' ),#
    path('reporteasesoria', vglobal.crearReporteView, name= "reporteasesoria"),
    
]
