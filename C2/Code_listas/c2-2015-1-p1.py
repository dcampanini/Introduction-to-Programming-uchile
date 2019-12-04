# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:41:34 2019

@author: Diego Campanini
"""
#============================= C2 2015-1 P1 ==================================
#%%
import estructura 
from lista import *

#%% crear estructura que representa a un polinomio p(x)=5x^3 + 3x
estructura.crear('coeficiente','valor potencia')
P=lista(coeficiente(5,3),lista(coeficiente(3,1),None))

#%% funcion para evaluar un polinomio, por ej p(10)=5*10^3 + 3*10
def evaluar(p,x):
    if p==None:
        return 0
    else:
        coef=cabeza(p).valor
        exponente=cabeza(p).potencia
        unaParte=coef*(x**exponente)
        return unaParte + evaluar(cola(p),x)

print
print 'p(10)=5*10^3 + 3*10 =',evaluar(P,10)

#%% funcion para evaluar p(x) para una lista de valores x
listax=lista(10,lista(1,lista(2,None)))

def evaluarLista(p,listax):
    if listax==None:
        return None
    else:
        x=cabeza(listax)
        pEvaluado=evaluar(p,x)
        return lista(pEvaluado,evaluarLista(p,cola(listax)))

print 
print 'p(x)=5x^3 + 3x  evaluado en 10,1,2 = ', evaluarLista(P,listax) 




#%%

















































