# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from tags.models import Tag
from actions import Normalizador

class Aviso(models.Model):
    titulo = models.CharField(max_length=225)
    contenido = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    imagen = models.ImageField(upload_to='items/avisos', blank=True, null=True)
    def __unicode__(self):
        return self.titulo

def update_UrlAviso(sender, instance, **kwargs):
    aviso = None
    urlNormal = Normalizador(instance.titulo)
    try:
        aviso =UrlAviso.objects.get(aviso=instance)
    except:
        pass
    if aviso:
        aviso.url = urlNormal
        aviso.save()
    else:
        aviso = UrlAviso()
        aviso.aviso = instance
        aviso.url = urlNormal
        aviso.save()

class UrlAviso(models.Model):
    aviso = models.ForeignKey('Aviso')
    url = models.CharField(max_length=225)
    def __unicode__(self):
        return self.url

post_save.connect(update_UrlAviso, sender=Aviso, dispatch_uid="update_url_avisos")