# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:31:36 2019

@author: Diego Campanini
"""
#%%
import estructura 
from lista import *

estructura.crear("carta", "calle ciudad pais")
c1 = carta("Lira 123", "Santiago", "Chile")
c2 = carta("Abaroa 2128", "Calama", "Chile")
c3 = carta("Vespucio 443", "Arica", "Chile")
c4 = carta("sn 111", "Calama", "Chile")
#
L0 = listaVacia
L1 = crearLista(c1, L0)
L2 = crearLista(c2, L1)
L3 = crearLista(c3, L2)
Lcartas = crearLista(c4, L3)

print "Carta 1= ", c1
print "Carta 2= ", c2
print "Carta 3= ", c3
print
print "Lista de Cartas= ", Lcartas

#%% funcion entrega True si una ciudad esta o False si no
def estaLaCiudad(Lcartas, ciudad):
    if vacia(Lcartas):
        return False
    else:
        # sera la ciudad que se busca?
        unaCarta = cabeza(Lcartas)
        if unaCarta.ciudad == ciudad:
            return True
        else:
            # si no es el caso, se revisa el resto de la lista
            resto = cola(Lcartas)
            return estaLaCiudad(resto, ciudad)
#%%
def contarCiudad(Lcartas, ciudad):
    if vacia(Lcartas):
        return 0
    else:
        unaCarta = cabeza(Lcartas)
        resto = cola(Lcartas)
        if unaCarta.ciudad == ciudad:
            # si es, se incrementa y se cuenta el resto
            return 1 + contarCiudad (resto, ciudad)
        else:
            # si no es, solo se cuenta el resto
            return contarCiudad(resto, ciudad)

#%% funcion para sacar una ciudad
def sacarCiudad(Lcartas, ciudad):
    if vacia(Lcartas):
        return listaVacia
    else:
        unaCarta = cabeza(Lcartas)
        resto = cola(Lcartas)
        if unaCarta.ciudad == ciudad:
            return sacarCiudad (resto, ciudad)
        else:
            restoLimpio = sacarCiudad(resto, ciudad)
            return crearLista(unaCarta, restoLimpio)
        

#%%



































