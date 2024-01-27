# Generated by Django 5.0 on 2024-01-27 03:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_estudiante_career_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_verificar', models.CharField(max_length=10)),
                ('carrera', models.CharField(choices=[('LFI', 'Licenciatura en Fisica'), ('LMT', 'Licenciatura en Matematicas'), ('INNI', 'Ingenieria en Informatica'), ('INCO', 'Ingenieria en Computacion'), ('QFB', 'Quimico Farmaceutico Biólogo')], default=1, max_length=100)),
                ('sexo', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Prefiero no decirlo'), (4, 'No binario')], default=1)),
                ('fecha_nacimiento', models.DateField()),
                ('asesorado', models.BooleanField(default=False)),
                ('telefono', models.CharField(max_length=10, verbose_name='')),
                ('estado_civil', models.IntegerField(choices=[(1, 'Soltero/Soltera'), (2, 'Matrimonio'), (3, 'Union Libre'), (4, 'Viudez')], default=1)),
                ('residencia', models.CharField(max_length=150, verbose_name='')),
                ('ciclo_admision', models.CharField(choices=[('18B', '2018B'), ('19A', '2019A'), ('19B', '2019B')], default='18B', max_length=3)),
                ('ciclo_actual', models.CharField(default='', max_length=3, verbose_name='')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilTutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_verificar', models.CharField(max_length=10)),
                ('sexo', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Prefiero no decirlo'), (4, 'No binario')], default=1)),
                ('fecha_nacimiento', models.DateField()),
                ('depto', models.CharField(choices=[('INNI', 'Informatica')], default=1, max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
