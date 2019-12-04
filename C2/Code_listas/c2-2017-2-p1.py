# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 02:50:00 2019

@author: Diego Campanini
"""
#%%
from lista import *
import math

#%% parte (a)
def esPrimo(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# esta funcion entrega la lista de primos pero en orden de mayor a menor
def my_listaPrimos(N,lprimos=listaVacia,num=3):
    if N==0:
        return lprimos
    else:
        if esPrimo(num):
            lprimos=crearLista(num,lprimos)
            return my_listaPrimos(N-1,lprimos,num+1)
        else:
            return my_listaPrimos(N,lprimos,num+1)

# solucion de la pauta del control
def listaPrimos(N,impar=3):
    #caso base: 0.3 ptos
    if N==0: return None
    #caso primo: 0.7 ptos
    if esPrimo(impar): #0.2
        #print 'lista primos=',lista(impar,listaPrimos(N-1,impar+2))
        return lista(impar,listaPrimos(N-1,impar+2)) #0.5
    #caso no primo: 0.3 ptos
    else: #opcional
        return listaPrimos(N,impar+2)


# programa
l0=listaPrimos(4)
print 'l0=',l0

#%% parte b
# esta funcion no esta bien implementada
'''def maximo(L,m=3):
    if cabeza(L)==listaVacia:
        print 'if'
        return  m
    else:
        print 'else'
        if cabeza(L)>m:
            m=cabeza(L)
            print m
            return maximo(cola(L),m)
        else:
            return maximo(cola(L),m)'''


#%% parte b
def my_primoMasCercano(N,L,cercano=3):
    if cabeza(L)>=N:
        return cercano
    elif cola(L)==None:
        return 0
    else:# equivalente a decir elif cabeza(L)>=N
        cercano=cabeza(cola(L))
        return my_primoMasCercano(N,cola(L),cercano)

#print 
mc=my_primoMasCercano(20,l0)
print
print 'mas cercano=',mc

#%% parte c

# funcion que invierte una lista
def invertir(L,linvertida=listaVacia):
    if L==None:
        return linvertida
    else:
        linvertida=crearLista(cabeza(L),linvertida)
        return invertir(cola(L),linvertida)

#####
def my_rangoPrimos(L,x,y,lrango=listaVacia):
    if L==None:
        return invertir(lrango)
    elif cabeza(L)<x:
        return my_rangoPrimos(cola(L),x,y)
    elif cabeza(L)>=x and cabeza(L)<=y:
        lrango=crearLista(cabeza(L),lrango)
        return my_rangoPrimos(cola(L),x,y,lrango)
    else:
        return invertir(lrango)
        

# programa
l1=listaPrimos(6)
print 'l1=',l1
print 
lrango=my_rangoPrimos(l1,4,20)
print 'lrango=',lrango

#%% 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        