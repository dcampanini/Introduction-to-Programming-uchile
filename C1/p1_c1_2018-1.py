# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 00:17:05 2019

@author: Diego Campanini
"""

#%%
# funcion con errores
def contiene1(number,digito):
    ultimo=number%10
    if digito==ultimo:
        return True
    else:
        return False or contiene1(number/10,digito)
    
#%%
def contiene(number,digito):
    if number<10:
        if digito==number:
            return True
        else:
            return False
    if number%10==digito:
        return True
    else:
        return contiene(number/10,digito)

def testcontiene():
    number=input('N?')
    if number<0:
        return 0
    else:
        s=contiene(number,0)
        if s==True:
            print 'Si'
        else:
            print 'No'
        return testcontiene()