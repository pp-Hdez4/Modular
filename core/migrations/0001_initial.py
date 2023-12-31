# Generated by Django 5.0 on 2023-12-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutoriaIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoEstudiante', models.IntegerField()),
                ('ApellidoPaterno', models.CharField(max_length=150)),
                ('ApellidoMaterno', models.CharField(max_length=150)),
                ('Nombres', models.CharField(max_length=150)),
                ('Telefono', models.IntegerField()),
                ('Genero', models.IntegerField(choices=[(0, 'Hombre'), (1, 'Mujer'), (2, 'Prefiero no decirlo'), (3, 'No binario')])),
                ('ProgramaEducativo', models.IntegerField(choices=[(0, 'Ingenieria en Computacion'), (1, 'Ingenieria en Informatica')])),
                ('Municipio', models.CharField(max_length=150)),
                ('FechaNacimiento', models.DateField()),
                ('EstadoCivil', models.IntegerField(choices=[(0, 'Soltero/Soltera'), (1, 'Matrimonio'), (2, 'Union Libre'), (3, 'Viudez')])),
                ('importancia', models.IntegerField(choices=[(1, '1 - Muy Bajo'), (2, '2 - Bajo'), (3, '3 - Moderado'), (4, '4 - Alto'), (5, '5 - Muy Alto')])),
                ('pregunta_radio', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
            ],
        ),
    ]
