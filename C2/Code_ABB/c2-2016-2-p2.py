# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:47:22 2019

@author: Diego Campanini
"""
#============================= C2 2016-2 P2 ==================================
#%%
import estructura #0.1
#%% ===== P2 (a) solucion 2 ========
p=True #0.1
q=False #0.1
r=False #0.1
estructura.crear("AB","valor izq der") #0.1
#arbol: 1.0
a=AB("and", AB(p,None,None), AB("not",None, \
     AB("or",AB(q,None,None),AB(r,None,None)))) 

#%% ===== P2 (b) solucion 2 ========

# my solution
def evaluar(a):
    if a==None:
        return
    if a.izq==None and a.der==None:
        return a.valor
    vizq=evaluar(a.izq)
    vder=evaluar(a.der)
    operador=a.valor
    if operador=='and':
        return vizq and vder
    elif operador=='or':
        return vizq or vder
    elif operador=='not':
        return not vder
print
print'valor del arbol= ', evaluar(a)