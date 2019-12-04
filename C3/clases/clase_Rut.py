# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:55:19 2019

@author: Diego Campanini
"""
#%% clase rut
class Rut:
    def __init__(self,unRut):
        self.__numero=unRut[0 : len(unRut) - 2]
        self.__verificador=unRut[len(unRut) - 1]
    
    def getNumero(self):
        return self.__numero
    
    def getVerificardo(self):
        return self.__verificador
    

#%% programa
r1= raw_input("Ingrese el Rut? ")
# transformar el rut en un objeto de la clase Rut
rut1=Rut(r1)
print 'El numero es:',rut1.getNumero()
print 'El digito verificador es:',rut1.getVerificardo()

    