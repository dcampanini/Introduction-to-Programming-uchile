# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:13:50 2019

@author: Diego Campanini
"""

#%% definicion clase Fraccion, pero sin sobrecarga de operadores
class Fraccion:
    # constructor
    def __init__(self,num=0,den=1):# creo que el 0 y 1 no son estrictamente necesarios
        # inicializacion de campos
        self.__numerador=num
        self.__denominador=den
    
    def __str__(self):
        return str(self.__numerador) 

    def __add__(self, f):
        num = self.__numerador * f.__denominador + f.__numerador * self.__denominador
        den = self.__denominador * self.__denominador
        return Fraccion(num, den)

    def __gt__(self, f):
        return self.__numerador * f.__denominador > f.__numerador * self.__denominador

#%% crear objeto de la clase Fraccion
f12=Fraccion(1,2)
f34=Fraccion(3,4)
f54=f12 + f34
print
print 'suma f12+f34=',f54

#printear la fraccion mayor
if f34 > f12:
    print 'mayor fraccion=',str(f34)
else:
    print 'mayor fraccion=',str(f12)


fn=f12+f12+f34
print 'fn=',str(fn)

#%%
















































