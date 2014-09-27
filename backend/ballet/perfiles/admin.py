from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from perfiles.models import Perfil, UrlPerfil, Genero, Telefono, TipoTelefono


class AdminPerfil(SummernoteModelAdmin):
	model = Perfil


admin.site.register(Perfil, AdminPerfil)
admin.site.register(Genero)
admin.site.register(Telefono)
admin.site.register(TipoTelefono)
