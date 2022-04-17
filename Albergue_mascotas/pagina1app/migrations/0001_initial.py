# Generated by Django 2.2.12 on 2022-04-17 19:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Registro_mascota',
            fields=[
                ('id_mascota', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_mascota', models.CharField(max_length=100)),
                ('sexo_mascota', models.IntegerField(choices=[[0, 'Macho'], [1, 'Hembra']])),
                ('edad_mascota', models.PositiveIntegerField()),
                ('fecha_rescate_mascota', models.DateField()),
                ('fecha_vacuna_mascota', models.DateField()),
                ('foto_mascota', models.ImageField(null=True, upload_to='fotos_mascotas')),
                ('raza_mascota', models.CharField(max_length=100)),
                ('vacunas_mascota', multiselectfield.db.fields.MultiSelectField(choices=[('rabia', 'Rabia'), ('distemper', 'Distemper'), ('leptospirosis', 'Leptospirosis'), ('hepatitis_canina', 'Hepatitis canina'), ('parainfluenza', 'Parainfluenza')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_adopcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.PositiveIntegerField()),
                ('domicilio', models.CharField(max_length=1000)),
                ('id_mascota', models.PositiveIntegerField()),
                ('razon', models.TextField()),
            ],
        ),
    ]
