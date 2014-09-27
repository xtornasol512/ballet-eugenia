# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301
from cultura.models import UrlPost, Post
from actions import Paginador

maximo_paginas=2


def index_view(request):
    #La iteracion es un compusto de las urls y la post.
    posts=UrlPost.objects.all()
    pagina = request.GET.get("pagina", "")
    if posts:
      posts = Paginador(posts, maximo_paginas, pagina)
    cxt = {'posts':posts, 'filtro':False}

    return render_to_response('cultura/listaPosts.html',
                          cxt,
                          context_instance=RequestContext(request))


def post(request, post):
    pal = None
    try:
        pal = UrlPost.objects.get(url=post)
        cxt = {'post':pal.post, 'url':pal.url}
    except :
        cxt = {'post':pal, 'url':None}

    return render_to_response('cultura/post.html',
                          cxt,
                          context_instance=RequestContext(request))


def tag_post(request, tag):
    posts=UrlPost.objects.filter(post__tags__tag__icontains=tag)
    pagina = request.GET.get("pagina", "")
    if posts:
      posts = Paginador(posts, maximo_paginas, pagina)
    cxt = {'posts':posts, 'filtro':True, 'tag':tag}

    return render_to_response('cultura/listaPosts.html',
                          cxt,
                          context_instance=RequestContext(request))

def busqueda_post(request):
    tag = request.GET.get("busqueda", "")
    posts = None
    if tag:
        posts=UrlPost.objects.filter(post__tags__tag__icontains=tag)
        pagina = request.GET.get("pagina", "")
        if posts:
          posts = Paginador(posts, maximo_paginas, pagina)
    cxt = {'posts':posts, 'filtro':True, 'tag':tag}

    return render_to_response('cultura/listaPosts.html',
                          cxt,
                          context_instance=RequestContext(request))