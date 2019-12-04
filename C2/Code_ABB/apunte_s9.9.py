# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:18:19 2019

@author: Diego Campanini
"""
#%%
import estructura 
from lista import *

# codigo para crear un arbol binario cualquiera ( no necesariamente un ABB)
estructura.crear("nodo","rut nombre izq der")
nodoVacio=None

# crearNodo : int str nodo nodo -> nodo
# devuelve un nodo ABB con datos rut , nombre
# y los nodos izq y der , respectivamente
def crearNodo(rut,nombre,izq,der):
    return nodo(rut,nombre,izq,der)

# vacio : nodo -> bool
# devuelve True si el ABB esta vacio
def vacio(nodo):
    return nodo==nodoVacio

# crear dos arboles binario
unArbol = crearNodo (15 , " Juan ", nodoVacio ,\
        crearNodo (24 , " Ivan ", nodoVacio , nodoVacio ))
otroArbol = crearNodo (15 , " Juan ",\
            crearNodo (87 , " Hector ", nodoVacio , nodoVacio ), nodoVacio )

#%% 
# codigo para buscar un rut dentro de un ABB

# encontrarNombre : ABB int -> str
# busca el nodo de un ABB cuyo rut es unRUT
# y retorna el texto asociado al nombre en dicho nodo
# ejemplo :
# si ABB = crearNodo (15 , " Juan ", nodoVacio , crearNodo (24 , " Ivan ",
#nodoVacio , nodoVacio ))
# entonces encontrarNombre (ABB , 24) devuelve " Ivan "
def encontrarNombre (unNodo , unRUT ):
    if vacio ( unNodo ):
        return ""
    else :
        if unRUT == unNodo.rut :
            return unNodo.nombre
        elif unRUT < unNodo.rut :
            return encontrarNombre ( unNodo.izq , unRUT )
        else : # unRUT > unNodo .rut
            return encontrarNombre ( unNodo.der , unRUT )


# Tests
ABB = crearNodo (15 , " Juan ", nodoVacio , crearNodo (24 , " Ivan ",\
nodoVacio , nodoVacio ))
assert encontrarNombre (ABB , 24) == " Ivan "
assert encontrarNombre (ABB , 50) == ""


#%% 
# codigo para printear los nodos en orden

# printea los nodos izquierdo del ultimo al nodo raiz
def enOrdenIzq(ABB):
    if vacio(ABB):
        return 
    else:
        enOrdenIzq(ABB.izq)
        print ABB.nombre

#printea los nodos derecho del raiz al ultimo
def enOrdenDer(ABB):
    if vacio(ABB):
        return 
    else:
        print ABB.nombre
        enOrdenDer(ABB.der)

#printea todos los nodos del arbol
def enOrden(ABB):
    if vacio(ABB):
        return 
    else:
        enOrden(ABB.izq)
        print ABB.nombre, ABB.rut
        enOrden(ABB.der)


# programa
print
abb2 = crearNodo( 15 , "Juan ", crearNodo(12,"Pedro",\
crearNodo(7,"Claudia",nodoVacio,nodoVacio),crearNodo(13,"Lili",nodoVacio,nodoVacio)),\
crearNodo (24 , "Ivan",crearNodo(20,"Diego",nodoVacio,nodoVacio),\
crearNodo(36,"Alejandro",nodoVacio,nodoVacio))  )

print 'Nodos Izq del ABB:'
enOrdenIzq(abb2)
print
print 'Nodos Der del ABB:'
enOrdenDer(abb2)
print
print 'Nodos del ABB:'
enOrden(abb2)

#%%













