# -*- coding: utf-8 -*-

# Importar módulos
import estructura
from lista import *

# nodo: valor (cualquier tipo) izq (nodo) der (nodo)
estructura.crear("nodo", "valor izq der")

# identificador para nodos vacios
nodoVacio = None

# Función para crear una estructura de tipo nodo
def crearNodo(valor, izq, der):
    return nodo(valor, izq, der)

# Función para crear un ABB vacío
def crearABB():
    return nodoVacio


# insertarABB: persona nodo -> nodo
# inserta un nodo con atributo valor en el ABB raiz
# el orden de los nodos está dado por el rut
def insertarABB(valor, raiz):
    if raiz == nodoVacio:
        return crearNodo(valor, nodoVacio, nodoVacio)
    else:
        # Test: no se pueden insertar rut repetido
        assert raiz.valor.rut != valor.rut
        # Si valor es menor, entonces se inserta recursivamente en el
        # subárbol izquierdo
        if valor.rut < raiz.valor.rut:
            return crearNodo(raiz.valor, insertarABB(valor, raiz.izq), raiz.der)
        # Si valor es mayor, entonces se inserta recursivamente en el
        # subárbol derecho
        else:
            return crearNodo(raiz.valor, raiz.izq, insertarABB(valor, raiz.der))
        
'''
Ejemplo de un árbol que almacena estructuras de tipo persona
'''
# persona: nombre (str) edad (int) rut (str)
estructura.crear("persona", "nombre edad rut")

# Ejemplos de personas
juan = persona("juan", 25, "11111111-1")
maria= persona("maria", 33, "77777777-7")
ana= persona("ana", 19, "12345678-9")

# Crear árbol con los ejemplos anteriores
raiz = crearABB()
raiz = insertarABB(juan, raiz)
raiz = insertarABB(maria, raiz)
raiz = insertarABB(ana, raiz)

# El árbol tiene la siguiente forma, debido al orden en que se
# insertaron los nodos:
#  juan
#      \
#       maria
#      /
#   ana


def escribirContenido_IRD(raiz):
    # caso base, no se imprime nada
    if raiz == nodoVacio:
        print " "
    else:
        # imprimir recursivamente los valores del subárbol de la
        # izquierda
        escribirContenido_IRD(raiz.izq)
        # imprimir el valor de la raíz
        persona = raiz.valor
        print "Nombre: " + persona.nombre
        print "Rut: " + persona.rut
        print "Edad: " + str(persona.edad)
        # imprimir recursivamente los valores del subárbol de la
        # derecha        
        escribirContenido_IRD(raiz.der)

# Ejemplo con el árbol creado anteriormente
escribirContenido_IRD(raiz)
