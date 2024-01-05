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

optionsRespons = [
    (0, "Yo"),
    (1, "Madre"),
    (2, "Padre"),
    (3, "Madre y Padre"),
    (4, "Tutor legal"),
    (5, "Hermanos, hermanas"),
    (6, "Pareja"),
    (7, "Otros"),
]

optionsVive = [
    (0, "Sola/Solo"),
    (1, "Pareja"),
    (2, "Padres"),
    (3, "En casa de asistencia o compartiendo vivienda con otras personas"),
    (4, "Otro")
]

mediosTrs = [
    (0, "Un solo medio de transporte público"),
    (1, "Dos o más medios de transporte público"),
    (2, "Automóvil"),
    (3, "Bicicleta"),
    (4, "Taxi"),
    (5, "Uber"),
    (6, "Otro"),
]

optionsTiempos = [
    (0, "De 15 a 30 minutos"),
    (1, "De 31 a 45 minutos"),
    (2, "De 46 a 60 minutos"),
    (3, "De 61 minutos a 2 horas"),
    (4, "Más de dos horas"),
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
    
class e_vivienda(models.Model):
    responsable_ecnm = models.IntegerField("En tu hogar donde vives actualmente, ¿Quién es la persona responsable del mayor aporte económico?", choices = optionsRespons, default = 0)
    viveAct = models.IntegerField("¿Con quién vives actualmente?", choices = optionsVive, default = 0)
    otro_vive = models.CharField("", max_length=150)
    apoyo_economico = models.IntegerField("¿Recibes algún apoyo económico? (como becas, subsidio, etc)", choices = rankingBool, default = 0)
    is_foraneo = models.CharField("¿Eres foráneo? (Si la respuesta es ""Si"" especifica de que estado procedes)", max_length = 400)

class e_tiemposTrs(models.Model):
    medio_trns = models.IntegerField("¿Qué medio de transporte utilizas regularmente para trasladarte a CUCEI?", choices = mediosTrs, default = 0)
    otro_trns = models.CharField("", max_length=150)
    timetransport = models.IntegerField("¿Cuánto tiempo aproximadamente te toma llegar diario a CUCEI desde tu casa?", choices = optionsTiempos, default = 0)
