# Generated by Django 5.0 on 2024-01-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_asesoria_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesoria',
            name='materia',
            field=models.CharField(choices=[('Programacion', 'Programacion'), ('Calculo', 'Calculo'), ('Pre calculo', 'Pre calculo'), ('Fisica', 'Fisica'), ('Algoritmia', 'Algoritmia')], max_length=30),
        ),
    ]
