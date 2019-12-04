# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 02:27:16 2019

@author: Diego Campanini
"""
#%%
import estructura
from lista import *

#%% crear abb de numeros
estructura.crear('arbol','valor izq der')
abb=arbol(50,arbol(40,arbol(10,None,None),arbol(45,None,None)),\
          arbol(100,arbol(70,None,None),arbol(90,None,None)))

#%% funcion para insertar un elemento x en un abb
estructura.crear("nodo","valor izq der")
def crearNodo(valor,izq,der):
    return nodo(valor,izq,der)

def insertar(x,abb): #0.1
    if abb==None: 
        return crearNodo(x,None,None) #0.5
    v=abb.valor #0.2
    if x<v: return crearNodo(v,insertar(x,abb.izq),abb.der) #0.5
    if x>v: return crearNodo(v,abb.izq,insertar(x,abb.der)) #0.5
    return abb
#%%
def filtrar(abb,X,Y,A=None): #0.1 (o llamar a otra función con None)
    if abb==None: #0.2
        return A #0.2
    #traspasar valores en el rango: 1.5 ptos
    v=abb.valor #0.2
    if X<=v and v<=Y: #0.3
        A=insertar(v,A) #1.0
    #recursión: 2.0 ptos
    A=filtrar(abb.izq,X,Y,A) #1.0
    return filtrar(abb.der,X,Y,A)


print
print 'abb original= ', abb
print
print 'abb filtrado= ', filtrar(abb,20,80)

#%% my filtrar (mala porque recorre solo la parte izquierda del arbol, a las 
# instrucciones para recorrer la parte derecha entra una vez que ya esta en 
# la parte izquierda del arbol)
#def my_filtrar(a,x,y,newAbb=None):
#    if a==None:
#        return newAbb
#    else:
#        if x < a.valor < y:
#            newAbb=insertar(a.valor,newAbb)
#            return my_filtrar(a.izq,x,y,newAbb)
#        elif x > a.valor and a.valor < y:
#            return my_filtrar(a.der,x,y,newAbb)
#        elif a.valor > y:
#            return my_filtrar(a.izq,x,y,newAbb)
#        
#
#
#print
#print 'abb original= ', abb
#print
#print 'abb filtrado= ', my_filtrar(abb,20,80)
#%%
    




























