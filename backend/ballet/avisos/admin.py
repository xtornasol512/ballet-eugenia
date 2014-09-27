from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from avisos.models import Aviso


class AdminAvisos(SummernoteModelAdmin):
	model = Aviso


admin.site.register(Aviso, AdminAvisos)