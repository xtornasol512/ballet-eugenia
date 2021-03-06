# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from actions import Normalizador
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario=models.ForeignKey(User, unique=True)
    biografia=models.TextField(blank=True, null=True)
    domicilio=models.TextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='perfiles/perfil', blank=True, null=True)
    edad = models.CharField(max_length=2, blank=True, null=True)
    genero = models.ForeignKey('Genero', blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    editable = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    def __unicode__(self):
        return "%s"%self.usuario

class Genero(models.Model):
    genero=models.CharField(max_length=10)
    def __unicode__(self):
        return self.genero

class Telefono(models.Model):
    tipo=models.ForeignKey('TipoTelefono')
    telefono = models.CharField(max_length=15)
    perfil = models.ForeignKey('Perfil')
    def __unicode__(self):
        return "%s - %s"%(self.perfil, self.telefono)

class TipoTelefono(models.Model):
    tipo=models.CharField(max_length=50)

class UrlPerfil(models.Model):
    perfil = models.ForeignKey('Perfil')
    url = models.CharField(max_length=225)
    def __unicode__(self):
        return self.url

def update_UrlPerfil(sender, instance, **kwargs):
    perfil = None
    if True:
        urlNormal = instance.usuario.username
        try:
            perfil =UrlPerfil.objects.get(perfil=instance)
        except:
            pass
        if perfil:
            perfil.url = urlNormal
            perfil.save()
        else:
            perfil = UrlPerfil()
            perfil.perfil = instance
            perfil.url = urlNormal
            perfil.save()

post_save.connect(update_UrlPerfil, sender=Perfil, dispatch_uid="update_url_perfil")