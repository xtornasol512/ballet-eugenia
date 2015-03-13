from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from avisos.models import Aviso, Tag


class AdminAvisos(SummernoteModelAdmin):
    model = Aviso
    filter_horizontal =('tags',)


admin.site.register(Aviso, AdminAvisos)
admin.site.register(Tag)