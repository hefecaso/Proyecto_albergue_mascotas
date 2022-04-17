from django.db import models
from datetime import datetime, date
from multiselectfield import MultiSelectField
# Create your models here.


#####################################
#   Creando sección de consultas    #
#####################################

opciones_consultas=[
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
        #Por cada clase agregada, hay que migrar
        #python manage.py makemigrations
        #python manage.py migrate

#############################################
#   Creación formulario Albergue_mascotas   #
#############################################

sexo_mascota_op =[
    [0, "Macho"],
    [1, "Hembra"],
]

vacunas_mascota_op = (
    ("rabia", "Rabia"),
    ("distemper", "Distemper"),
    ("leptospirosis", "Leptospirosis"),
    ("hepatitis_canina", "Hepatitis canina"),
    ("parainfluenza", "Parainfluenza")
)

class Registro_mascota(models.Model):
    id_mascota = models.PositiveIntegerField(primary_key=True)
    nombre_mascota = models.CharField(max_length=100)
    sexo_mascota = models.IntegerField(choices=sexo_mascota_op)
    edad_mascota = models.PositiveIntegerField()
    fecha_rescate_mascota = models.DateField(auto_now_add=False, auto_now=False)
    fecha_vacuna_mascota = models.DateField(auto_now_add=False, auto_now=False)
    foto_mascota = models.ImageField(upload_to = 'fotos_mascotas', null=True)
    raza_mascota = models.CharField(max_length=100)
    vacunas_mascota = MultiSelectField(choices=vacunas_mascota_op)
    def __str__(self):
        return self.nombre_mascota


class Solicitud_adopcion(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField()
    telefono = models.PositiveIntegerField()
    domicilio = models.CharField(max_length=1000)
    id_mascota = models.PositiveIntegerField()
    razon = models.TextField()

    def __str__(self):
        return self.nombres

#Para postgres
#DROP DATABASE puppy_heroe;
#create database puppy_heroe;


#Para las fotos:
#https://www.youtube.com/watch?v=miaOMvHw4nw&t=178s&ab_channel=codigofacilito
#https://youtu.be/D94NBN4bO1g?t=94
#https://www.youtube.com/watch?v=KSFCQud4avc&ab_channel=moisessepulveda

#Referencia formularios
# https://www.youtube.com/watch?v=HDz6lqZ91rE&t=554s
# https://www.youtube.com/watch?v=B3oQIx1W8PA&t=662s
