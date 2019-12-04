# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:52:48 2019

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



#%% printear el contenido del  ABB creado anteriormente de menor a mayor
def escribirContenido_IRD(raiz):
    if raiz == nodoVacio:
        print ''
    else:
        escribirContenido_IRD(raiz.izq)
        persona=raiz.valor
        print 'Nombre:'+persona.nombre
        print 'Rut:'+persona.rut
        print 'Edad:'+ str(persona.edad)
        escribirContenido_IRD(raiz.der)

# programa
escribirContenido_IRD(raiz)

#%% crear un string con todo el contenido del arbol

def contenidoEnString(raiz):
    if raiz==nodoVacio:
        return ''
    else:
        persona=raiz.valor
        texto=' Nombre: '+ persona.nombre
        texto=texto+' Rut: '+ persona.rut
        texto=texto+' Edad: '+ str(persona.edad)
        return contenidoEnString(raiz.izq) + texto + \
                contenidoEnString(raiz.der)
                
# programa
print
print contenidoEnString(raiz)


#%% contar la cantidad de nodos no vacios de un arbol
def contarNodos(raiz):
    if raiz == nodoVacio:
        return 0
    else:
        return 1+contarNodos(raiz.izq)+contarNodos(raiz.der)

# programa
print 
print 'cantidad de nodos= ',contarNodos(raiz)        
    
#%% 
def my_balanceado(raiz):
    total_izq=contarNodos(raiz.izq)
    total_der=contarNodos(raiz.der)
    if raiz==nodoVacio:
        return True
    elif math.fabs(total_izq-total_der)<1.0:
        return True
    else:
        return False

# programa
print
print 'es balanceado? ',my_balanceado(raiz)

def balanceado(raiz):
    if raiz ==nodoVacio:
        return True
    else:
        total_izq=contarNodos(raiz.izq)
        total_der=contarNodos(raiz.der)
        if math.fabs(total_izq - total_der)>1:
            return False
        else:
            return balanceado(raiz.izq) and balanceado(raiz.der)

# programa
print
print 'es balanceado (profe)? ',balanceado(raiz)


#%% determinar la profundidad de un arbol binario
def profundidad(raiz):
    if raiz==nodoVacio:
        return 0
    else:
        prof_izq=profundidad(raiz.izq)
        prof_der=profundidad(raiz.der)
        return 1+max(prof_izq,prof_der)

# programa
print
print 'profundidad arbol binario=',profundidad(raiz)




#%%
# ============================================================================
# ========================== Codigos JAlvarez ================================
# ============================================================================

#%% determinar el numero de nodos hoja (ie sin hijos) en un Arbol Binario, no
# necesariamente ABB
def hojas(raiz):
     if raiz==nodoVacio:
         return 0
     else:
         if raiz.izq==nodoVacio and raiz.der==nodoVacio:
             return 1
         else:
             return hojas(raiz.izq) + hojas(raiz.der)

print
print 'cantidad de nodos hoja en AB= ', hojas(raiz)

#%% mi version de la funcion que cuenta los nodos no hojas en un AB
def my_nohojas(raiz):
    if raiz==nodoVacio:
        return 0
    elif (raiz.izq==nodoVacio and raiz.der==nodoVacio):
        return 0
    else:
        if raiz.izq!=nodoVacio or raiz.der!=nodoVacio:
            return 1 + my_nohojas(raiz.izq) + my_nohojas(raiz.der)

print
print 'nodos no hojas en AB (my version)= ', my_nohojas(raiz)
     
# version del profe  
def nohojas(raiz):
    return profundidad(raiz)-hojas(raiz)

print
print 'nodos no hojas en AB (version profe)= ', nohojas(raiz)

#%% Funcion que entrega True si un arbol binario (AB) es un ABB




#%% funcion para buscar un valor x en un ABB
# x es lo que busco, A=ABB
def enABB(x,A):
    if A==None: return False
    if x<A.valor: return enABB(x,A.izq)
    if x>A.valor: return enABB(x,A.der)
    return True  #x==A.valor
    
print
juan = persona('juan', 25, '11111111-1')
print 'esta x en el abb? ', enABB(juan,raiz)



#%%

























