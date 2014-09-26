# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301
from diccionario.models import UrlPalabra, Palabra


def index_view(request):
    #La iteracion es un compusto de las urls y la palabra.
    palabras=UrlPalabra.objects.all()
    cxt = {'palabras':palabras, 'filtro':False}

    return render_to_response('diccionario/listaPalabras.html',
                          cxt,
                          context_instance=RequestContext(request))


def palabra(request, palabra):
    pal = None
    try:
        pal = UrlPalabra.objects.get(url=palabra)
        cxt = {'palabra':pal.palabra, 'url':pal.url}
    except :
        cxt = {'palabra':pal, 'url':None}

    return render_to_response('diccionario/palabra.html',
                          cxt,
                          context_instance=RequestContext(request))


def tag_palabra(request, tag):
    palabras=UrlPalabra.objects.filter(palabra__tags__tag__icontains=tag)
    cxt = {'palabras':palabras, 'filtro':True, 'tag':tag}

    return render_to_response('diccionario/listaPalabras.html',
                          cxt,
                          context_instance=RequestContext(request))

def busqueda_palabra(request):
    tag = request.GET.get("busqueda", "")
    palabras = None
    if tag:
        palabras=UrlPalabra.objects.filter(palabra__tags__tag__icontains=tag)
    cxt = {'palabras':palabras, 'filtro':True, 'tag':tag}

    return render_to_response('diccionario/listaPalabras.html',
                          cxt,
                          context_instance=RequestContext(request))