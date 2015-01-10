# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from actions import Normalizador
from django.contrib.auth.models import User


class Grupo(models.Model):
    literal = models.CharField(max_length=1, unique=True, verbose_name='Grupo')
    descripcion = models.TextField()
    profesor = models.CharField(default="Miss Gennita", max_length=255)
    def __unicode__(self):
        return "Grupo %s"%self.literal

class Alumno(models.Model):
    grupo = models.ForeignKey("Grupo")
    nombre = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return "%s - Grupo %s"%(self.nombre, self.grupo.literal)
    def usuario(self):
        usu=UsuarioAlumno.objects.get(alumno=self)
        return usu.usuario.username


class UsuarioAlumno(models.Model):
    usuario = models.ForeignKey(User)
    alumno = models.ForeignKey("Alumno")
    def __str__(self):
        return "%s"%self.alumno

def update_UsuarioAlumno(sender, instance, **kwargs):
    if not UsuarioAlumno.objects.filter(alumno=instance).exists():
        nickNormalizado = Normalizador(instance.nombre)
        aux=nickNormalizado
        count=1
        while (User.objects.filter(username=aux).exists()):
            aux="%s%s"%(nickNormalizado,count)
            count = count + 1
        nickNormalizado=aux
        user = User.objects.create_user(nickNormalizado, instance.email, 'ballet.alumno')
        usAl=UsuarioAlumno()
        usAl.usuario=user
        usAl.alumno=instance
        usAl.save()

post_save.connect(update_UsuarioAlumno, sender=Alumno, dispatch_uid="update_usuario_alumno")