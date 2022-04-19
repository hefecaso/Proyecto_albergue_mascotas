from  django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import Contacto, Registro_mascota, Solicitud_adopcion

class CustomUserCreationForm(UserCreationForm):
    pass

class ContactoForm(forms.ModelForm):
    #Tomamos datos desde el modelo definido en models
    class Meta:
        model = Contacto
        #Asegurarse que los siguientes campos estén en el modelo, aparecera en el orden escrito
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        #Otra opción, para que aparezca en el orden que tiene en modelo.py podríamos escribir lo siguiente:
        #fields = '__all__'

class Registro_mascota_Form(forms.ModelForm):
    #Tomamos datos desde el modelo definido en models
    class Meta:
        model = Registro_mascota
        #Asegurarse que los siguientes campos estén en el modelo, aparecera en el orden escrito
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        #Otra opción, para que aparezca en el orden que tiene en modelo.py podríamos escribir lo siguiente:
        fields = '__all__'
        '''[
        'id_mascota',
        'nombre_mascota',
        'sexo_mascota',
        'edad_mascota',
        'fecha_rescate_mascota',
        'fecha_vacuna_mascota',
        'raza_mascota',
        'vacunas_mascota',
        ]'''

        labels ={
            'id_mascota': 'ID de la mascota #DDMMAAAAK',
            'nombre_mascota': 'Nombre de la mascota',
            'sexo_mascota': 'Sexo de la mascota',
            'edad_mascota': 'Edad de la mascota',
            'fecha_rescate_mascota': 'Fecha de rescate (DD/MM/AAAA)',
            'fecha_vacuna_mascota': 'Fecha de vacunación (DD/MM/AAAA)',
            'foto_mascota':'Foto de la mascota',
            'raza_mascota': 'Raza de la mascota',
            'vacunas_mascota': 'Vacunas de la mascota',
        }


class Solicitud_adopcion_Form(forms.ModelForm):
    #Tomamos datos desde el modelo definido en models
    class Meta:
        model = Solicitud_adopcion
        #Asegurarse que los siguientes campos estén en el modelo, aparecera en el orden escrito
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        #Otra opción, para que aparezca en el orden que tiene en modelo.py podríamos escribir lo siguiente:
        fields = '__all__'

        labels ={
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'correo': 'Correo',
            'telefono': 'Teléfono',
            'domicilio': 'Domicilio',
            'id_mascota': 'ID de la mascota',
            'razon': 'Razón de la adopción',
        }



'''
Referencias:
https://www.youtube.com/watch?v=90M4gunBRLs&t=174s&ab_channel=moisessepulveda
'''
