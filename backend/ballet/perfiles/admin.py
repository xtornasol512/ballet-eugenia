from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from diccionario.models import Palabra, UrlPalabra, Tag


class AdminPalabra(SummernoteModelAdmin):
	model = Palabra


admin.site.register(Palabra, AdminPalabra)
#el URL palabra es la relacion de urls amigables, por lo que no deve ser editable
#admin.site.register(UrlPalabra)
admin.site.register(Tag)