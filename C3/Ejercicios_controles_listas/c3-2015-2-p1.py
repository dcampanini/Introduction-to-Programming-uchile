# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:50:22 2019

@author: Diego Campanini
"""
#%%
import estructura 
from lista import *

estructura.mutable('invitado','nombre confirmado')
#%% c3 2015-2 p1 (a)

# funcion para invitar o no a un amigo
def invitar(amigos):
    lista_inv=[]
    for am in amigos:
        r=raw_input('Invitar a '+am+' si o no? ')
        if r=='si':
            inv=invitado(am,False)
            lista_inv=lista_inv+[inv]
    return lista_inv

#%% p1 (b): funcion para que los invitados confirmen
def confirmar(invitados,confirmados):
    for i in range(len(invitados)):
        p=invitados[i]
        if p.nombre in confirmados:
            invitados[i].confirmado=True
    return invitados

#%% p1 (c): funcion para listar los invitados

def listar(invitados):
    inv=[]
    for i in range(len(invitados)):
        c=invitados[i].confirmado
        if c==True:
            inv=inv+[invitados[i].nombre]
    inv.sort()
    for p in inv:
        print
        print p

#%% probar funcion
amigos=['Juan', 'Ana', 'Rosa', 'Jose', 'Nico']
invitados=invitar(amigos)
print '\ninvitados= ',invitados
invitados_conf=confirmar(invitados,['Nico','Rosa'])
print
print 'lista con confirmados= ', invitados_conf
print
print 'lista de confirmados orden alfabetico'
listar(invitados_conf)

#%%















































