from django.urls import path, include
#importamos de la primer app lo relacionado
#a las vistas
from pagina1app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth import views as auth_views #Password reset

urlpatterns = [

    path('',views.home, name="Home"),
    path('servicios/',views.servicios, name="Servicios"),
    path('albergue/',views.albergue, name="Albergue"),
    #path('iniciosesion',views.iniciosesion, name="Inicio de sesión"),
    path('contacto/',views.contacto, name="Contacto"),
    path('registro_y_adopcion/',views.registro_y_adopcion, name="Formularios registro y adopcion"),
    path('formulario_registro_mascota/',views.formulario_registro_mascota, name="Formulario registro"),
    path('formulario_adopcion/',views.formulario_adopcion, name="Formulario adopcion"),
    path('registro/',views.registro, name="Formulario Registro"),

    #Configurando restablecer contraseña
    #Video: https://www.youtube.com/watch?v=sFPcd6myZrY&ab_channel=DennisIvy
    #Documentación actualizada: https://docs.djangoproject.com/en/4.0/topics/auth/default/
    path('accounts/password_reset/',
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
        name = "password_reset"),

    path('accounts/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name = "password_reset_done"),

    path('accounts/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
        name = "password_reset_confirm"),

    path('accounts/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name = "password_reset_complete"),


    #Personalizando tema en admin
    #path('jet/', include('jet.urls', 'jet')),
    #path('admin/', include(admin.site.urls)),
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard'))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
1 - Submit email form                           //PasswordResetView.as_view()
2 - Email sent succes massage                   //PasswordResetDoneView.as_view()
3 - Link to password Reset form in email        //PasswordResetConfirmView.as_view()
4 - Password succesfully changed message        //PasswordResetCompleteVies.as_view()
'''
