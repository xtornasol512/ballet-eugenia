# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301

def index_view(request):
    usuario = None
    ctx = { "user" : usuario }
    return render_to_response('home/index.html',
                          ctx,
                          context_instance=RequestContext(request))

def missgennita(request):
    return render_to_response('home/missgennita.html',
                          context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('home/contacto.html',
                          context_instance=RequestContext(request))

def reglamento(request):
    return render_to_response('home/reglamento.html',
                          context_instance=RequestContext(request))

def login(request):
    return render_to_response('home/login.html',
                          context_instance=RequestContext(request))

def academia(request):
    return render_to_response('home/academia.html',
                          context_instance=RequestContext(request))

def calendario(request):
    return render_to_response('home/calendario.html',
                          context_instance=RequestContext(request))