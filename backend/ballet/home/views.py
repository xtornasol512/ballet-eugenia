# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect as redirect301

from actions2 import UrlUsuario

def index_view(request):
    
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def missgennita(request):
    #usuario = request.user
    #ctx = { "user" : usuario }
    return render_to_response('home/missgennita.html',
                          context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('home/contacto.html',
                          context_instance=RequestContext(request))

def reglamento(request):
    return render_to_response('home/reglamento.html',
                          context_instance=RequestContext(request))

def log_in(request):
    usuario=request.user
    if usuario.is_anonymous():
        error=None
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            #solicitud de login por post
            acceso=authenticate(username=username,password=password)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    #Pantalla del Perfil
                    return HttpResponseRedirect('/')
                else:
                    error="Posiblemente tu usuario este baneado o desactivado, comunicate con el administrador"
            else:
                error="El usuario no existe, o la contraseña esta mal escrita, verifique sus datos"
        ctx={"error":error}
        return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
    else:
        url_user=UrlUsuario(usuario)
        return HttpResponseRedirect('%s/'%url_user)

@login_required(login_url='/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def academia(request):
    return render_to_response('home/academia.html',
                          context_instance=RequestContext(request))

def calendario(request):
    return render_to_response('home/calendario.html',
                          context_instance=RequestContext(request))