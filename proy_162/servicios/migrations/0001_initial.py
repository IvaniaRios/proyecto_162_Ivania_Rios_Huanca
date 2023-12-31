# Generated by Django 5.0 on 2023-12-13 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('Medio día', 'Medio día'), ('Tiempo Completo', 'Tiempo Completo'), ('Tarde', 'Tarde'), ('Noche', 'Noche'), ('Mañana', 'Mañana')], max_length=50)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('descripcion', models.TextField()),
                ('dia_semana', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sueldo', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('appat', models.CharField(max_length=50)),
                ('apmat', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('genero', models.CharField(choices=[('masculino', 'masculino'), ('femenino', 'femenino')], max_length=15)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('ci', models.CharField(max_length=15)),
                ('fecha_reg', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('appat', models.CharField(max_length=50)),
                ('apmat', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('genero', models.CharField(choices=[('masculino', 'masculino'), ('femenino', 'femenino')], max_length=15)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('ci', models.CharField(max_length=15)),
                ('fecha_reg', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HorarioMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.horario')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.medico')),
            ],
        ),
        migrations.CreateModel(
            name='EspecialidadMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.especialidad')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.medico')),
            ],
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('motivo', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('atendido', models.BooleanField(default=False)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.paciente')),
            ],
        ),
    ]
