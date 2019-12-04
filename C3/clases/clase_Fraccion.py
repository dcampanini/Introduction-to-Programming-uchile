# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:09:16 2019

@author: Diego Campanini
"""

#%% definicion clase Fraccion
class Fraccion:
    # constructor
    def __init__(self,num=0,den=1):# creo que el 0 y 1 no son estrictamente necesarios
        # inicializacion de campos
        self.__numerador=num
        self.__denominador=den
    
    # getNumerador: None -> int
    # devuelve el valor del campo numerador
    def getNumerador(self):
        tipo=self.__tipoNum
        return self.__numerador
       
    # toString: None -> str
    # devuelve un string con la fraccion
    def toString(self):
        return str(self.__numerador) + "/" + str(self.__denominador)
    
    # suma: Fraccion -> Fraccion
    # devuelve la suma de la fraccion con otra fraccion
    def suma(self, unaFraccion):
        num = self.__numerador * unaFraccion.__denominador + \
        unaFraccion.__numerador * self.__denominador
        den = self.__denominador * unaFraccion.__denominador
        return Fraccion(num, den)

#%% crear objeto de la clase Fraccion
f12=Fraccion(1,2)
f34=Fraccion(3,4)
f54=f12.suma(f34)
print
print 'numerador objeto f12=',f12.getNumerador()
print
print 'suma f12+f34=',f54.toString()



#%%










































