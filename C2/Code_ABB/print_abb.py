# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:05:47 2019

@author: Diego Campanini
"""

#%% 
import math
import estructura 
from lista import *
estructura.crear("nodo","valor izq der")

def crearNodo(valor,izq,der):
    return nodo(valor,izq,der)

nodoVacio=None
def crearABB():
    return nodoVacio

#%% ej crear ABB con numeros

# funcion para insertar un nodo a la izquierda o derecha de un nodo raiz, que 
# puede ser un nodo cualquiera
def insertarABB_num(valor,raiz):
    if raiz==nodoVacio:
        # si es un nodo vacio se le agrega un valor y se crean el nodo izq y 
        # der vacios
        return crearNodo(valor,nodoVacio,nodoVacio)
    else:
        if valor < raiz.valor:
            # agregar nodo a la izquierda
            return crearNodo(raiz.valor, insertarABB_num(valor,raiz.izq), raiz.der)
        else:
            return crearNodo(raiz.valor, raiz.izq, insertarABB_num(valor,raiz.der))

# programa
raiz = crearABB()
raiz = insertarABB_num(100, raiz)
raiz = insertarABB_num(65, raiz)
raiz = insertarABB_num(180, raiz)
print
print raiz

#%% crear un ABB usando para crearlo el rut ie rut pequeños a la izq y rut 
# grandes a la derecha

def insertarABB(valor, raiz):
    if raiz == nodoVacio:
        return crearNodo(valor, nodoVacio, nodoVacio)
    else:
        # Test: no se pueden insertar rut repetido
        assert raiz.valor.rut != valor.rut
        # Insercion
        if valor.rut < raiz.valor.rut:
            return crearNodo(raiz.valor, insertarABB(valor,raiz.izq), raiz.der)
        else: # valor.rut > raiz.rut
            return crearNodo(raiz.valor, raiz.izq, insertarABB(valor,raiz.der))


# programa
# El árbol tiene la siguiente forma, debido al orden en que se
# insertaron los nodos:
#  juan
#      \
#       maria
#      /
#   ana

estructura.crear('persona', 'nombre edad rut')
juan = persona('juan', 25, '11111111-1')
maria= persona('maria', 33, '77777777-7')
ana= persona('ana', 19, '12345678-9')
raiz = crearABB( )
print raiz
raiz = insertarABB(juan, raiz)
print
print raiz
raiz = insertarABB(maria, raiz)
print
print raiz
raiz = insertarABB(ana, raiz)
print
print raiz

#%% creacion abb2
juan = persona('juan', 25, '11111111-1')
maria= persona('maria', 33, '77777777-7')
ana= persona('ana', 19, '12345678-9')
diego=persona('diego', 33, '11111110-0')

abb2 = crearABB( )
abb2 = insertarABB(juan, abb2)
abb2 = insertarABB(maria, abb2)
abb2 = insertarABB(ana, abb2)
abb2 = insertarABB(diego, abb2)
print
print abb2

#%% creacion abb3
juan = persona('juan', 25, '11111111-1')

maria= persona('maria', 33, '77777777-7')
ana= persona('ana', 19, '12345678-9')
jose = persona('jose',1,'9999999999-9')

diego=persona('diego', 33, '11111000-0')
ines=persona('ines', 33, '11110000-0')
july=persona('july', 33, '11111110-0')

abb3 = crearABB( )
abb3 = insertarABB(juan, abb3)
# subarbol izq
abb3 = insertarABB(maria, abb3)
abb3 = insertarABB(ana, abb3)
abb3 = insertarABB(jose, abb3)
# subarbol derecho
abb3 = insertarABB(diego, abb3)
abb3 = insertarABB(ines, abb3)
abb3 = insertarABB(july, abb3)


print
print abb3



#%% printear abb en "pre order"
# este codigo printea raiz-izq-derecha
def preOrder(raiz):
    if raiz==nodoVacio:
        return
    else:
        persona=raiz.valor
        print 'Nombre:'+persona.nombre
        print 'Rut:'+persona.rut
        print 'Edad:'+ str(persona.edad)
        preOrder(raiz.izq)
        preOrder(raiz.der)

print
print 'ABB1 en pre order= \n',preOrder(raiz)
print
print 'ABB2 en pre order= \n',preOrder(abb2)
print
print 'ABB3 en pre order= \n',preOrder(abb3)
                                      



#%% printear abb en 'post order'
# este codigo printea izq-der-raiz
def postOrder(raiz):
    if raiz==nodoVacio:
        return
    else:
        postOrder(raiz.izq)
        postOrder(raiz.der)
        persona=raiz.valor
        print 'Nombre:'+persona.nombre
        print 'Rut:'+persona.rut
        print 'Edad:'+ str(persona.edad)


print
print 'ABB1 en post order= \n',postOrder(raiz)
print
print 'ABB2 en post order= \n',postOrder(abb2)
print
print 'ABB3 en post order= \n',postOrder(abb3)


#%%







































