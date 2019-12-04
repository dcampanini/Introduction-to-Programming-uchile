# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:43:12 2019

@author: Diego Campanini
"""
#%%
import estructura
estructura.crear("fraccion", "numerador denominador")
f=fraccion(1,2)

def sumaFraccion(f1, f2):
    numerador = f1.numerador * f2.denominador + f2.numerador * f1.denominador
    denominador = f1.denominador * f2.denominador
    f3 = fraccion(numerador , denominador)
    return f3

#%% usar la funcion sumaFraccion
f1=fraccion(1,2)
f2=fraccion(1,4)
f3=sumaFraccion(f1,f2)
print 'f3=',f3