# Generated by Django 5.0 on 2024-01-18 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_usuario_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='career',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.programaeducativo'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ciclo_admision',
            field=models.CharField(choices=[('18B', '2018B'), ('19A', '2019A'), ('19B', '2019B')], default='18B', max_length=3),
        ),
    ]