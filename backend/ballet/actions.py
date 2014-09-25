# -*- coding: utf-8 -*-
from unicodedata import normalize

def Normalizador(txt):
	#Normalizar texto
	txt = normalize('NFKD', txt).encode('ascii', 'ignore')
	#pasar a minusculas
	txt = txt.lower()
	#quitar espacios y poner -
	txt = '-'.join( txt.split() )
	return txt