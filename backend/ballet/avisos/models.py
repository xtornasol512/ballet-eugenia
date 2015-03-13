# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from actions import Normalizador
from usuarios.models import Alumno
from ballet.settings import API_KEY

import mandrill
 


class Aviso(models.Model):
    titulo = models.CharField(max_length=225)
    contenido = models.TextField()
    tags = models.ManyToManyField("Tag", null=True, blank=True, verbose_name='Etiquetas')
    imagen = models.ImageField(upload_to='items/avisos', blank=True, null=True)
    vigencia = models.DateField(blank=True, null=True)
    borrador = models.BooleanField(default=False)
    archivo = models.FileField(upload_to='archivos/adjuntos', blank=True, null=True)
    def __unicode__(self):
        return self.titulo


#clase para futuros multiples archivos adjuntos
'''
class ArchivosAviso(models.Model):
    aviso = models.ForeignKey(Aviso)
    archivo = models.FileField(upload_to='archivos/adjuntos')
    nombre = models.CharField(blank=True, null=True, max_length=50)
    def __unicode__(self):
        if self.nombre:
            codigo="archivo %s de %s"%(self.nombre,self.aviso)
        else:
            codigo="archivo adjunto de %s"%(self.aviso)
        return codigo'''

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

def update_UrlAviso(sender, instance, **kwargs):
    if not instance.borrador:
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
        #  . . . . . . . envio de avisos por correo
        #lista de correos (complementar a correos no repetidos despues)
        alumnos= Alumno.objects.filter(activo=True).exclude(email=None)
        para=[]
        for alum in alumnos:
            para.append({"email":alum.email, "name": alum.nombre, "type": "bcc"})

        #archivos adjuntos
        codAdjun=""
        if instance.archivo:
            codAdjun="<br><h3>Archivos Adjuntos</h3><br><a href='http://ballet-eugenia.com/media/%s'>Archivo Adjunto</a>"%(instance.archivo)


        #enviar el correo
        mandrill_client = mandrill.Mandrill(API_KEY)

        message = {
            "html": "%s%s"%(instance.contenido, codAdjun),
            "subject": instance.titulo,
            "from_email": "genny@ballet-eugenia.com",
            "from_name": "Miss Gennita",
            "to": para
        }
        result = mandrill_client.messages.send(message=message, async=False)

class UrlAviso(models.Model):
    aviso = models.ForeignKey('Aviso')
    url = models.CharField(max_length=225)
    def __unicode__(self):
        return self.url

post_save.connect(update_UrlAviso, sender=Aviso, dispatch_uid="update_url_avisos")