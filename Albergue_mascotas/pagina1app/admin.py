from django.contrib import admin
from .models import Contacto, Registro_mascota, Solicitud_adopcion
from django.contrib.auth.models import Group
#Creando configuración para exportar e importar documentos
#from import_export import resources
from import_export.admin import ImportExportModelAdmin


#class PuppyHeroeAdmin(admin.ModelAdmin):
    #exclude = ('title',)
    #fields = ('title',)
    #list_display = ('title', 'created')
    #list_filter = ('created')
        #No funcionó o no entendí XD
    #change_list_template = 'admin/puppy_heroe_admin/admin_dashboard.html'

# Register your models here.

#admin.site.register(Contacto)
#admin.site.register(Registro_mascota)
#admin.site.register(Solicitud_adopcion)

#Con unregister desaparecemos un campo en el admin
admin.site.unregister(Group)
#admin.site.unregister(Temas)

#Cambiando título de Djadmin
admin.site.site_header = "Puppy Heroe - Admin dashboard"

'''
#Creando configuración para exportar e importar documentos
class ContactoAdminResource(resources.ModelResource):

    class Meta:
        model   =   Contacto
'''

@admin.register(Contacto)
class Contacto_Admin(ImportExportModelAdmin):
    list_display = (
    'nombre',
    'correo',
    'tipo_consulta',
    'mensaje',
    'avisos'
    )
    pass

@admin.register(Registro_mascota)
class Registro_mascota_Admin(ImportExportModelAdmin):
    list_display = (
    'id_mascota',
    'nombre_mascota',
    'sexo_mascota',
    'edad_mascota',
    'fecha_rescate_mascota',
    'fecha_vacuna_mascota',
    'foto_mascota',
    'raza_mascota',
    'vacunas_mascota',
    )
    pass

@admin.register(Solicitud_adopcion)
class Solicitud_adopcion_Admin(ImportExportModelAdmin):
    list_display = (
    'nombres',
    'apellidos',
    'edad',
    'correo',
    'telefono',
    'domicilio',
    'id_mascota',
    'razon',
    )
    pass
