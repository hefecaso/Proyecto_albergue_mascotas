from import_export import resources
from .models import Contacto, Registro_mascota, Solicitud_adopcion

class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto
