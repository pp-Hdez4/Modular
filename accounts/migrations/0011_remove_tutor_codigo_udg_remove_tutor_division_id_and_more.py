# Generated by Django 5.0 on 2024-01-28 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_perfilestudiante_perfiltutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='codigo_udg',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='division_id',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]
