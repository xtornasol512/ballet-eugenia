# -*- coding: utf-8 -*-
from unicodedata import normalize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

def Normalizador(txt):
    #Normalizar texto
    txt = normalize('NFKD', txt).encode('ascii', 'ignore')
    #pasar a minusculas
    txt = txt.lower()
    #quitar espacios y poner -
    txt = '-'.join( txt.split() )
    #quita caracteres que no sean letras, numeros o -
    txt = re.sub("[^\w\-]", "", txt)
    return txt

def Paginador(objetos, maximo, pagina):
    paginado = Paginator(objetos, maximo)
    try:
        paginado = paginado.page(pagina)
    except PageNotAnInteger:
        paginado = paginado.page(1)
    except EmptyPage:
        paginado = paginado.page(paginado.num_pages)
    return paginado