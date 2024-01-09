from django.db import models
from django import forms

# Create your models here.
OpcionesGenero = [
    [1,"Hombre"],
    [2,"Mujer"],
    [3,"Prefiero no decirlo"],
    [4,"No binario"]
]

OpcionesProgramaEducativo = [
    [1,"Ingenieria en Computacion"],
    [2,"Ingenieria en Informatica"]
]

OpcionesEstadoCivil = [
    [1 ,"Soltero/Soltera"],
    [2,"Matrimonio"],
    [3,"Union Libre"],
    [4,"Viudez"]
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
    (1, "Tabaco"),
    (2, "Marihuana"),
    (3, "Otro: "),
]

times_drugs = [
    (1, "De 1 a 3"),
    (2, "De 3 a 5"),
    (3, "De 5 a 10"),
    (4, "Mas de 10"),
    (5, "Ocasionalmente"),
]

times_alcohol = [
    (1, "Diario"),
    (2, "Una o dos veces por semana"),
    (3, "Mas de 2 veces por semana"),
]

HorasTrabajadas = [
    (1, "Menos de 10"),
    (2, "De 10 a 20"),
    (3, "De 21 a 40"),
]

IngresoMensual = [
    (1, "$2,600 a $6,000"),
    (2, "$6,001 a $10,000"),
    (3, "10,001 a $32,000"),
    (4, "32,001 a $81,000"),
    (5, "Mas de $81,000"),
]

optionsRespons = [
    (1, "Yo"),
    (2, "Madre"),
    (3, "Padre"),
    (4, "Madre y Padre"),
    (5, "Tutor legal"),
    (6, "Hermanos, hermanas"),
    (7, "Pareja"),
    (8, "Otros"),
]

optionsVive = [
    (1, "Sola/Solo"),
    (2, "Pareja"),
    (3, "Padres"),
    (4, "En casa de asistencia o compartiendo vivienda con otras personas"),
    (5, "Otro")
]

mediosTrs = [
    (1, "Un solo medio de transporte público"),
    (2, "Dos o más medios de transporte público"),
    (3, "Automóvil"),
    (4, "Bicicleta"),
    (5, "Taxi"),
    (6, "Uber"),
    (7, "Otro"),
]

optionsTiempos = [
    (1, "De 15 a 30 minutos"),
    (2, "De 31 a 45 minutos"),
    (3, "De 46 a 60 minutos"),
    (4, "De 61 minutos a 2 horas"),
    (5, "Más de dos horas"),
]

prankingoptions3 = [
    (1, "Si"),
    (0, "No"),
    (2, "Prefiero no decirlo"),
]

lgbtcommnunity = [
    (1, "Cisgénero"),
    (2, "Transgénero"),
    (3, "Transexual"),
    (4, "No Binario"),
    (5, "Prefiero no responder"),
    (6, 'Otro: '),
]

opcionesneuro = [
    ("Autismo", "Autismo: transtorno del desarrollo que se incluye dentro del espectro autista y que afecta la interacción social recíproca, la comunicaión verbal y no verbal, una resistencia para aceptar el cambio, inflexibilidad del pensamiento así como poseer campos de interés estrechos y absorbentes"),
    ("Asperger", "Asperger: transtorno del desarrollo que se incluye dentro del espectro autista y que afecta la interacción social recíproca, la comunicación verbal y no verbal, una resistencia para aceptar el cambio, inflexibilidad del pensamiento así como poseer campos de interés estrechos y absorbentes."),
    ("Discalculia", "Discalculia: dificulta la comprensión de las matemáticas y las tareas relacionadas."),
    ("Dislexia", "Dislexia: dificultad en la lectura debido a inconvenientes para identificar los sonidos del habla y aprender a relacionarlos con las letras y las palabras"),
    ("Dispraxia", "Dispraxia: trastorno psicomotriz que se da en la infancia y hace que los movimientos que requieren la movilización y coordinación de varios grupos musculares"),
    ("Hiperactividad", "Trastorno por Déficit de Atención e Hiperactividad: problemas para prestar atención, controlar conductas impulsivas (podrían actuar sin pensar en el resultado de sus acciones) o pueden ser demasiados activos"),
    ("Tourette", "Síndrome de Tourette: se caracteriza por muchos tics motores y fónicos que perduran durante más de un año."),
    ("No", "No"),
    ("Otro", "Otro: "),
]

opcionSangre = [
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-"),
    ("Otro", "Otro: ")
]

opcionsaludmental = [
    (1, "Nunca"),
    (2, "Algunas veces"),
    (3, "Frecuentemente"),
    (4, "Casi siempre"),
    (5, "Siempre")
]

opcionesestilos = [
    (2, "Auditivo: Estilo se orienta más hacia la asimilación de información a través del oído, depende de escuchar y hablar como maneras principales para su aprendizaje, estas personas dialogan tanto como interna como externamente."),
    (1, "Visual: Ocurre cuando uno tiende a pensar en imágenes y a relacionarlas con ideas y conceptos. Como por ejemplo cuando uno recurre a mapas conceptuales para recordar ideas, conceptos y procesos complejos. Por lo mismo, éste sistema está directamente relacionado con nuestra capacidad de abstracción y planificación."),
    (3, "Knestésico: En otras palabras, es lo que ocurre cuando aprendemos más fácilmente al movernos y tocar las cosas, como cuando caminamos al recitar información o hacemos un experimento manipulando instrumentos de laboratorio."),
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
    smoke = models.IntegerField("¿Fumas?", choices = rankingBool, default = 0)
    w_smoke = models.IntegerField("¿Si la respuesta es si, qué es lo que fumas?", choices = drugs_types, default = 1)
    other_smoke = models.CharField("", max_length=150)
    t_smoke = models.IntegerField("Si la respuesta es si, ¿Cuántas dosis al día?", choices = times_drugs, default = 1)
    drinks_alcohol = models.IntegerField("¿Consumes bebidas con alcohol?", choices = rankingBool, default = 0)
    t_alcohol = models.IntegerField("Si la respuesta es si, ¿Con qué frecuencia?", choices = times_alcohol, default = 1)

class EmpleoIngresos(models.Model):
    TrabajoActual = models.BooleanField("¿Trabajas actualmente?", choices = rankingBool, default = 0)
    TrabajoRelacionadoCarrera = models.BooleanField("¿Tu trabajo actual esta relacionado con la carrera que estudias?", choices = rankingBool, default = 0)
    HorasTrabajadasSemana = models.BooleanField("¿Trabajas actualmente?", choices = HorasTrabajadas, default = 1)
    IngresoMensualTrabajo = models.BooleanField("Por favor indica a cuanto asciende tu ingreso mensual aproximadamente si trabajas:", choices = IngresoMensual, default = 1)
    AportacionEconomicaImportancia = models.BooleanField("Senala que tan importante es su aportacion economica en tu hogar a partir de la siguiente escala:", choices = OpcionesPregunta, default = 1)
    
class e_vivienda(models.Model):
    responsable_ecnm = models.IntegerField("En tu hogar donde vives actualmente, ¿Quién es la persona responsable del mayor aporte económico?", choices = optionsRespons, default = 1)
    viveAct = models.IntegerField("¿Con quién vives actualmente?", choices = optionsVive, default = 1)
    otro_vive = models.CharField("", max_length=150)
    apoyo_economico = models.IntegerField("¿Recibes algún apoyo económico? (como becas, subsidio, etc)", choices = rankingBool, default = 0)
    is_foraneo = models.CharField("¿Eres foráneo? (Si la respuesta es ""Si"" especifica de que estado procedes)", max_length = 400)

class e_tiemposTrs(models.Model):
    medio_trns = models.IntegerField("¿Qué medio de transporte utilizas regularmente para trasladarte a CUCEI?", choices = mediosTrs, default = 1)
    otro_trns = models.CharField("", max_length=150)
    timetransport = models.IntegerField("¿Cuánto tiempo aproximadamente te toma llegar diario a CUCEI desde tu casa?", choices = optionsTiempos, default = 1)

class mpueblos_orig(models.Model):
    comunidad = models.CharField("", max_length=150)
    lengua = models.CharField("", max_length=150)

class mpersonal(models.Model):
    comunidadlgbt = models.IntegerField("¿Perteneces a una comunidad LGBTTTIQ+?", choices = prankingoptions3, default = 0)
    identidadGen = models.IntegerField("Identidad de Genéro", choices = lgbtcommnunity, default = 1)
    other_identidad = models.CharField("", max_length=150)
    hijos = models.IntegerField("¿Tienes hijos?", choices = rankingBool, default = 0)
    hijoscuidado = models.IntegerField("¿Están a tu cuidado hijos u otros menores?", choices = rankingBool, default = 0)
    avanzcuidado = models.IntegerField("¿Cuidas de una persona en edad avanzada, enfermo o con capacidades diferentes?", choices = rankingBool, default = 0)

class mdiscapacidad(models.Model):
    es_discapacidad = models.IntegerField("¿Tienes alguna discapacidad?", choices = rankingBool, default = 0)
    tipod = models.CharField("", max_length=150)
    dispositivo_d = models.IntegerField("¿Usas o necesitas algún tipo de dispositivos de asistencia? Por ejemplo: silla de ruedas, bastones, muletas, prótesis, audífonos, etc.", choices = rankingBool, default = 0)
    tipodispositivod = models.CharField("", max_length=150)

class mneurodiversidad(models.Model):
    tipoNeurodiversidad = models.CharField("¿Consideras que te encuentras en una de las siguientes condiciones de neurodiversidad? :", choices = opcionesneuro, default = "No", max_length=150)
    otrotipo_neuro = models.CharField("", max_length=150)
    diagnostico = models.IntegerField("¿Tienes diágnostico de un médico?", choices = rankingBool, default = 0)
    tratamiento = models.IntegerField("En caso de haber contestado SI a la pregunta anterior, ¿Estás en tratamiento?", choices = rankingBool, default = 0)
    zurdo = models.BooleanField("Soy zurda/zurdo", default = False)
    enfermedad_celiaca = models.BooleanField("Enfermedad celíaca (alergía al gluten)", default = False)
    talla_baja = models.BooleanField("Soy persona de talla baja", default = False)
    is_not = models.BooleanField("No", default = False)

class msalud(models.Model):
    tiposangre = models.CharField("Tipo de Sangre: ", choices = opcionSangre, default = "O-", max_length = 100)
    otro_sangre = models.CharField("", max_length = 10)
    enfermedad_salud = models.CharField("", max_length = 100)
    alergias = models.CharField("", max_length = 100)

class msaludmental(models.Model):
    suenio = models.IntegerField("Dificultades para conciliar el sueño", choices = opcionsaludmental, default = 1)
    cansancio = models.IntegerField("Cansancio o fatiga que te impiden realizar algunas actividades", choices = opcionsaludmental, default = 1)
    fobias = models.IntegerField("Miedos incontrolables o fobias a objetos, personas o situaciones", choices = opcionsaludmental, default = 1)
    irritacion = models.IntegerField("Irritación o mal humor",choices = opcionsaludmental, default = 1)
    ansiedad = models.IntegerField("Ansiedad o angustia generalizada que te impide concentrarte",choices = opcionsaludmental, default = 1)
    motivacion = models.IntegerField("Motivación para hacer tus actividades cotidianas", choices = opcionsaludmental, default = 1)
    pensamientos = models.IntegerField("Pensamientos sobre quitarte la vida", choices = opcionsaludmental, default = 1)
    tristeza = models.IntegerField("Experimento tristeza", choices = opcionsaludmental, default = 1)
    felicidad = models.IntegerField("En general, me siento feliz", choices = opcionsaludmental, default = 1)
    terapia = models.IntegerField("¿Acudes a terapia psicológica o tratamiento psiquiátrico?", choices = rankingBool, default = 0)


class maccesotics(models.Model):
    pc = models.BooleanField("Computadora", default = False)
    telefono = models.BooleanField("Télefono inteligente", default = False)
    tableta = models.BooleanField("Tableta", default = False)
    ninguno = models.BooleanField("Ninguno de los anteriores", default = False)
    internet = models.IntegerField("¿Cuentas con internet propio?", choices = rankingBool, default = 1)
    lugar_estudio = models.CharField("", max_length = 100)
    horas = models.CharField("", max_length = 100)
    nmaterias = models.CharField("", max_length = 10)
    horasclases = models.CharField("", max_length = 10)
    horaslibres = models.CharField("", max_length = 10)
    perfil = models.IntegerField("¿Conoces el perfil de egreso de tu programa educativo?", choices = rankingBool, default = 1)
    malla = models.IntegerField("¿Conoces la malla curricular de tu programa educativo?", choices = rankingBool, default = 1)
    materias_pre = models.IntegerField("¿Sabes que materias llevan pre-requisito en tu malla curricular", choices = rankingBool, default = 1)
    estilos_aprendizaje = models.IntegerField("", choices = opcionesestilos, default = 1)
