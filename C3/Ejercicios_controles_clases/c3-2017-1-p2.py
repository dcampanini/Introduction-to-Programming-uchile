# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:44:16 2019

@author: Diego Campanini
"""

#%% c3 2017-1 p2 (b)
class Libro:
    def __init__(self,code,title):
        self.__codigo=code
        self.__titulo=title
        self.__lector=None
    
    def prestar(self,unlector):
        if self.__lector==None:
            self.__lector=unlector
            return True
        else:
            return False
    
    def lector(self):
        return self.__lector

#%% p2 (a)
def porcentajePrestados(listaLibros):
    total=len(listaLibros)
    prestados=0
    for unLibro in listaLibros:
        if unLibro.lector()!=None:
            prestados=prestados+1
    return 100.0*prestados/total

#%% formar lista de objetos de la clase libro
l1=Libro('1','papelucho')
l2=Libro('2','serway')
l3=Libro('3','principia')
listaLibros=[l1,l2,l3]
# prestados inicialmente
print
print 'porcentaje prestados inicialmente= ', porcentajePrestados(listaLibros)
# presta un libro
l1.prestar('juan')
print
print 'libro l1 prestado a: ', l1.lector()
print 'libro l2 prestado a: ', l2.lector()
print 'libro l3 prestado a: ', l3.lector()
print 
print'porcentaje prestados final= ', porcentajePrestados(listaLibros)
    

   
#%%






















































    