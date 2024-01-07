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
    (1, ""),
    (2, ""),
    (3, ""),
    (4, ""),
    (5, ""),
    (6, ""),
]

rankingOptions3 = [
    (1, "Tengo una idea de negocio que me gustaria impulsar"),
    (2, "Estoy desarollando un proyecto de emprendimiento, pero no lo he puesto en marcha"),
    (3, "Ninguna de las anteriores"),
]

rankingBool = [
    (1, "Si"),
    (0, "No"),
]

drugs_types = [
    (0, "Tabaco"),
    (1, "Marihuana"),
    (2, "Otro: "),
]

times_drugs = [
    (0, "De 1 a 3"),
    (1, "De 3 a 5"),
    (2, "De 5 a 10"),
    (3, "Mas de 10"),
    (4, "Ocasionalmente"),
]

times_alcohol = [
    (0, "Diario"),
    (1, "Una o dos veces por semana"),
    (2, "Mas de 2 veces por semana"),
]

HorasTrabajadas = [
    (0, "Menos de 10"),
    (1, "De 10 a 20"),
    (2, "De 21 a 40"),
]

IngresoMensual = [
    (0, "$2,600 a $6,000"),
    (1, "$6,001 a $10,000"),
    (2, "10,001 a $32,000"),
    (3, "32,001 a $81,000"),
    (4, "Mas de $81,000"),
    
    
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
    Recomendacion = models.IntegerField(choices=OpcionesPregunta, default=1)
    
    
    
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

class emprendimiento(models.Model):
    is_emprendimiento = models.IntegerField("¿Tienes alguna idea o proyecto de emprendimieto?", choices = rankingBool, default = 1)
    is_interesting = models.IntegerField("¿Te interesa emprender?", choices = rankingBool, default = 0)
    if_option = models.IntegerField("Si respondiste ""si"" a la pregunta anterior, por favor, selecciona la opcion de acuerdo con tu situación", choices = rankingOptions3, default = 1)
    tools_udg = models.BooleanField("¿Conoces las herramientas que la U de G ofrece para desarrollar y dar seguimiento a tu emprendimiento?", choices = rankingBool, default = 0)
    is_community = models.BooleanField("¿Te interesaria formar parte de alguna comunidad de emprendimiento para seguir desarrollando tus habilidades?", choices = rankingBool, default = 0)

class adicciones(models.Model):
    smoke = models.IntegerField("¿Fumas?", choices = rankingBool, default = 1)
    w_smoke = models.IntegerField("¿Si la respuesta es si, qué es lo que fumas?", choices = drugs_types, default = 0)
    other_smoke = models.CharField("", max_length=150)
    t_smoke = models.IntegerField("Si la respuesta es si, ¿Cuántas dosis al día?", choices = times_drugs, default = 0)
    drinks_alcohol = models.IntegerField("¿Consumes bebidas con alcohol?", choices = rankingBool, default = 1)
    t_alcohol = models.IntegerField("Si la respuesta es si, ¿Con qué frecuencia?", choices = times_alcohol, default = 0)

class EmpleoIngresos(models.Model):
    TrabajoActual = models.BooleanField("¿Trabajas actualmente?", choices = rankingBool, default = 0)
    TrabajoRelacionadoCarrera = models.BooleanField("¿Tu trabajo actual esta relacionado con la carrera que estudias?", choices = rankingBool, default = 0)
    HorasTrabajadasSemana = models.BooleanField("¿Trabajas actualmente?", choices = HorasTrabajadas, default = 0)
    IngresoMensualTrabajo = models.BooleanField("Por favor indica a cuanto asciende tu ingreso mensual aproximadamente si trabajas:", choices = IngresoMensual, default = 0)
    AportacionEconomicaImportancia = models.BooleanField("Senala que tan importante es su aportacion economica en tu hogar a partir de la siguiente escala:", choices = OpcionesPregunta, default = 0)
    