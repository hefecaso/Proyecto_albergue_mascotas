from django.contrib import admin
from .models import Contacto, Registro_mascota, Solicitud_adopcion

# Register your models here.

admin.site.register(Contacto)
admin.site.register(Registro_mascota)
admin.site.register(Solicitud_adopcion)
