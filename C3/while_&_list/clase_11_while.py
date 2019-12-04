# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 02:01:38 2019

@author: Diego Campanini
"""

#%% codigos con while
# siOno
def siOno(mensaje):
    texto = mensaje + " (si o no) ? "
    respuesta = raw_input (texto)
    while respuesta != "si" and respuesta != "no" :
        respuesta = raw_input (texto)
        #respuesta = respuesta # se lleva a minuscula
    return respuesta

#%% probar siOno(mensaje)
siOno('me quieres')
print 'yo no'

#%% calcular una serie
def masMenos1Divn(n):
    total=0
    i=1
    while i<=n:
        t=(1.0/i)*(-1)**(i+1)
        total=total+t
        i=i+1
    return total

print
print 'serie hasta n= ',masMenos1Divn(10)


