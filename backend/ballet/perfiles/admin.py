from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from perfiles.models import Perfil, UrlPerfil, Genero, Telefono, TipoTelefono

class TelefonoEnLinea(admin.StackedInline):
    model = Telefono
    extra = 1

class AdminPerfil(SummernoteModelAdmin):
    model = Perfil
    inlines=[TelefonoEnLinea,]


admin.site.register(Perfil, AdminPerfil)
admin.site.register(Genero)
admin.site.register(Telefono)
admin.site.register(TipoTelefono)
admin.site.register(UrlPerfil)
