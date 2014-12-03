from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from diccionario.models import Palabra, Tag


class AdminPalabra(SummernoteModelAdmin):
	model = Palabra


admin.site.register(Palabra, AdminPalabra)
admin.site.register(Tag)