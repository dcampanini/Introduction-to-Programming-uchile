# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:46:49 2019

@author: Diego Campanini
"""
#============================= C2 2015-2 P2 ==================================
#%%
import estructura 
from lista import *
#%% crear estructura y la lista con estas estructuras
estructura.crear('registro','palabra frecuencia')
r1=registro('la',2)
r2=registro('hi',3)
r3=registro('si',10)
# crear lista con registros
lreg=lista(r1,lista(r2,lista(r3,None)))


#%%  ===== P2 (a) my solution ========
def actualizar(p,lreg):
    if lreg==None:
        newreg=registro(p,1)
        return lista(newreg,None)
    else:
        unregistro=cabeza(lreg)
        if p==unregistro.palabra:
            newreg=registro(p,unregistro.frecuencia+1)
            nlista=lista(newreg,cola(lreg))
            return nlista
        else:# si p no esta en lreg
            nlista=lista(unregistro,actualizar(p,cola(lreg)))
            return nlista

print
print 'old lista de registros=',lreg
print
print 'new lista de registros= ',actualizar('lala',lreg)


#%% ===== P2 (b) my solution ========

#%% crear arbol
estructura.crear('registro','palabra frecuencia')
r1=registro('la',2)
r2=registro('el',1)
r3=registro('las',2)
r4=registro('los',3)

estructura.crear('arbol','valor izq der')
a=arbol(r1, arbol(r2,arbol(r4,None,None),None), arbol(r3,None,None) )

#%%
#función para concatenar dos listas: 0.5 ptos
def juntar(L1,L2):
    if L1==None: 
        return L2 #0.1
    return lista(cabeza(L1),juntar(cola(L1),L2)) #0.4

def aLista(A): #0.5 ptos
    if A==None: 
        return None #0.1
    return juntar(aLista(A.izq),lista(A.valor,aLista(A.der)))


# funcion que recibe un arbol binario transformado a una lista (arbolLista) 
# y determina las palabras con frecuencia mayor a x
def mayores_listas(arbolLista,x,n=0):
    if arbolLista==None:
        return n
    else:
        unReg=cabeza(arbolLista)
        if unReg.frecuencia > x:
            n=n+1
            return mayores_listas(cola(arbolLista),x,n)
        else:
            return mayores_listas(cola(arbolLista),x,n)

# funcion que recibe un arbol binario y determina las palabras con 
# frecuencia mayor a x
def my_mayores(a,x):
    arbolLista=aLista(a)
    return mayores_listas(arbolLista,x,n=0)

# probrar
print 
print 'frecuencia mayores a x=1 : ', my_mayores(a,1)
#%% ===== P2 (b)  control solution ========
def mayores(A,X): #0.1
    #caso base (árbol vacio): 0.3 ptos
    if A==None: 
        return 0
    #si frecuencia>X, sumar 1: 1.5 ptos
    reg=A.valor #0.2
    if reg.frecuencia>X: #0.3
        return 1 + mayores(A.izq,X) + mayores(A.der,X) #1.0
    else: #opcional
        #si frecuencia>X, sumar 0: 1.0 ptos
        return mayores(A.izq,X)+mayores(A.der,X)
    
print 
print 'frecuencia mayores a x=1 : ',mayores(a,1)

#%%
    










































