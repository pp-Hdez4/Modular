# Generated by Django 5.0 on 2024-01-15 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_usuariomodel_remove_tutorm_codigo_udg_tutormodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tutorModel',
            new_name='Tutor',
        ),
        migrations.RenameModel(
            old_name='usuarioModel',
            new_name='Usuario',
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo_admision', models.CharField(default='', max_length=3, verbose_name='')),
                ('ciclo_actual', models.CharField(default='', max_length=3, verbose_name='')),
                ('telefono', models.CharField(max_length=10, verbose_name='')),
                ('asesorado', models.BooleanField(default=False)),
                ('residencia', models.CharField(max_length=150, verbose_name='')),
                ('estado_civil', models.IntegerField(choices=[(1, 'Soltero/Soltera'), (2, 'Matrimonio'), (3, 'Union Libre'), (4, 'Viudez')], default=1)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.programaeducativo')),
                ('codigo_udg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='estudianteModel',
        ),
    ]