# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 01:50:51 2019

@author: Diego Campanini
"""

#%%
def cuenta(digito,number):
    if number <10:
        if number==digito:
            return 1
        else:
            return 0
    if number%10==digito:
        return 1+cuenta(digito,number/10)
    else:
        return cuenta(digito,number/10)

def moda(numero,digito=0,resultado=0):
    print 'digito=',digito
    if digito>9:
        return resultado
    if cuenta(digito,numero)>cuenta(resultado,numero):
        resultado=digito
        print 'resultado=',resultado
    return moda(numero,digito+1,resultado)
        