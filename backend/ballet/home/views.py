# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301

def index_view(request):
    cxt = {}

    return render_to_response('home/index.html',
                          cxt,
                          context_instance=RequestContext(request))
#Privacidad
def missgennyta(request):
    return render_to_response('privacidad/terminos_privacidad.html',
                          my_data_dict,
                          context_instance=RequestContext(request))


    contacto
    reglamento
    login