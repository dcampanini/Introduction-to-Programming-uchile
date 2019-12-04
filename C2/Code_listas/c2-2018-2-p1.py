# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:02:50 2019

@author: Diego Campanini
"""
#%%
from lista import *

l0=listaVacia
l1=crearLista(20,l0)
l2=crearLista(40,l1)
lnum=crearLista(30,l2)
# parte a
def eliminar(lnum,n,c=1):
    if c==n:
        return cola(lnum)
    else:
        c=c+1
        return crearLista(cabeza(lnum),eliminar(cola(lnum),n,c))

# programa
print
print 'lnum original=',lnum
print 'lnum eliminada=',eliminar(lnum,2)