# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301
from avisos.models import UrlAviso, Aviso
from actions import Paginador

maximo_paginas=20


def index_view(request):
    #La iteracion es un compusto de las urls y la aviso.
    avisos=UrlAviso.objects.all()
    pagina = request.GET.get("pagina", "")
    if avisos:
      avisos = Paginador(avisos, maximo_paginas, pagina)
    cxt = {'avisos':avisos, 'filtro':False}

    return render_to_response('avisos/listaAvisos.html',
                          cxt,
                          context_instance=RequestContext(request))


def aviso(request, aviso):
    pal = None
    try:
        pal = UrlAviso.objects.get(url=aviso)
        cxt = {'aviso':pal.aviso, 'url':pal.url}
    except :
        cxt = {'aviso':pal, 'url':None}

    return render_to_response('avisos/aviso.html',
                          cxt,
                          context_instance=RequestContext(request))


def tag_aviso(request, tag):
    avisos=UrlAviso.objects.filter(aviso__tags__tag__icontains=tag)
    pagina = request.GET.get("pagina", "")
    if avisos:
      avisos = Paginador(avisos, maximo_paginas, pagina)
    cxt = {'avisos':avisos, 'filtro':True, 'tag':tag}

    return render_to_response('avisos/listaAvisos.html',
                          cxt,
                          context_instance=RequestContext(request))

def busqueda_aviso(request):
    tag = request.GET.get("busqueda", "")
    avisos = None
    if tag:
        avisos=UrlAviso.objects.filter(aviso__tags__tag__icontains=tag)
        pagina = request.GET.get("pagina", "")
        if avisos:
          avisos = Paginador(avisos, maximo_paginas, pagina)
    cxt = {'avisos':avisos, 'filtro':True, 'tag':tag}

    return render_to_response('avisos/listaAvisos.html',
                          cxt,
                          context_instance=RequestContext(request))