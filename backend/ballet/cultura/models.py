# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from actions import Normalizador

class Post(models.Model):
    titulo = models.CharField(max_length=225)
    contenido = models.TextField()
    tags = models.ManyToManyField("Tag", null=True, blank=True, verbose_name='Etiquetas')
    imagen = models.ImageField(upload_to='items/posts', blank=True, null=True)
    def __unicode__(self):
        return self.titulo

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

def update_UrlPost(sender, instance, **kwargs):
    post = None
    urlNormal = Normalizador(instance.titulo)
    try:
        post =UrlPost.objects.get(post=instance)
    except:
        pass
    if post:
        post.url = urlNormal
        post.save()
    else:
        post = UrlPost()
        post.post = instance
        post.url = urlNormal
        post.save()

class UrlPost(models.Model):
    post = models.ForeignKey('Post')
    url = models.CharField(max_length=225)
    def __unicode__(self):
        return self.url

post_save.connect(update_UrlPost, sender=Post, dispatch_uid="update_url_post")