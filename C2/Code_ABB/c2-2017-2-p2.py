# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:23:22 2019

@author: Diego Campanini
"""
#============================= C2 2017-2 P2 ==================================
#%%
import estructura 
from lista import *

#%% crear estruturas que se almacenaran en un arbol

#alumno: nombre(str) sexo(str)
estructura.crear('alumno','nombre sexo')
#arbol: valor(alumno) izq(arbol) der(arbol)
estructura.crear('arbol','valor izq der')

# crear arbol
abb=arbol(alumno('jose','M'),\
arbol(alumno('gabi','F'),arbol(alumno('ana','F'),None,None),None),\
arbol(alumno('rosa','F'),None,None))


#%% ===== P2 (a) ========

# my solution
def mybuscar(name,abb,n=0):
    if abb==None:
        return n+1 # ojo aqui yo habia puesto solo 'n', pero para que 
                  # coincida con lo del profe es n+1
    else:
        if name < abb.valor.nombre:
            n=n+1
            return mybuscar(name,abb.izq,n)
        elif name > abb.valor.nombre:
            n=n+1
            return mybuscar(name,abb.der,n)
        else:# name == abb.valor.nombre
            n=n+1
            return n

print 
print 'numero de llamadas= ',mybuscar('ana',abb,n=0)

#%% pauta solution
def buscar(nombre, A):
    #caso nombre no encontrado: 0.3 ptos
    if A==None: #0.1
        return 1 #0.2
    #caso nombre encontrado: 1.0 ptos
    c=cmp(nombre,A.valor.nombre) #0.5
    if c==0: #0.2
        return 1 #0.3
    #buscar en arbol izq o der: 1.5 ptos
    if c<0: #0.2
        return 1 + buscar(nombre,A.izq) #0.6
    else: #0.1 (opcional)
        return 1 + buscar(nombre,A.der) #0.6

print 
print 'numero de llamadas= ',buscar('matias',abb)


#%% ===== P2 (b) solucion 1 ========

#función para concatenar dos listas: 0.5 ptos
def juntar(L1,L2):
    if L1==None: 
        return L2 #0.1
    return lista(cabeza(L1),juntar(cola(L1),L2)) #0.4


#listaSexo: arbol str -> lista
def listaSexo(A,sexo):
    #caso base: 0.2 ptos
    if A==None: 
        return None
    #listas de arboles iq y der: 0.6
    L1=listaSexo(A.izq,sexo) #0.3
    L2=listaSexo(A.der,sexo) #0.3
    #seleccionar por sexo: 1.0 ptos
    if A.valor.sexo==sexo: #0.5
        L2=lista(A.valor.nombre,L2) #0.5
    #concatenar listas: 0.5 ptos
    return juntar(L1,L2)


print
print 'lista con un sexo= ', listaSexo(abb,'F')

#%% ===== P2 (b) solucion 2 ========
def listaSexo(A,sexo):
    #convertir arbol en lista: 0.2
    L=aLista(A)
    #filtrar por sexo: 0.4 ptos
    L=filtro(L, lambda x,y: x.sexo==y, sexo)
    #convertir a lista de nombres: 0.2 ptos
    return listaNombres(L)

# funcion que transforma arbol a lista
def aLista(A): #0.5 ptos
    if A==None: 
        return None #0.1
    return juntar(aLista(A.izq),lista(A.valor,aLista(A.der)))
 
print                
print 'abb como lista= ',aLista(abb)

def juntar(L1,L2): #0.5 ptos
    if L1==None: return L2 #0.1
    return lista(cabeza(L1),juntar(cola(L1),L2)) #0.4

def filtro(L,f,x): #0.5 ptos
    if L==None: return None #0.1
    v=cabeza(L)
    L=filtro(cola(L),f,x) #0.1
    if f(v,x): 
        return lista(v,L) #0.2
    return L #0.1

def listaNombres(L): #0.5 ptos
    if L==None: return None #0.1
    return lista(cabeza(L).nombre,listaNombres(cola(L))) #0.4


print
print 'lista con un sexo (sol alternativa)= ', listaSexo(abb,'F')

#%%



















