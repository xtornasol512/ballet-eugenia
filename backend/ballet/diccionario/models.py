# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from actions import Normalizador

class Palabra(models.Model):
    titulo = models.CharField(max_length=225)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='items/palabras', blank=True, null=True)
    def __unicode__(self):
        return self.titulo

def update_UrlPalabra(sender, instance, **kwargs):
	palabra = None
	urlNormal = Normalizador(instance.titulo)
	try:
		palabra =UrlPalabra.objects.get(palabra=instance)
	except:
		pass
	if palabra:
		palabra.url = urlNormal
		palabra.save()
	else:
		palabra = UrlPalabra()
		palabra.palabra = instance
		palabra.url = urlNormal
		palabra.save()

class UrlPalabra(models.Model):
	palabra = models.ForeignKey('Palabra')
	url = models.CharField(max_length=225)
	def __unicode__(self):
		return self.url

post_save.connect(update_UrlPalabra, sender=Palabra, dispatch_uid="update_url_palabra")