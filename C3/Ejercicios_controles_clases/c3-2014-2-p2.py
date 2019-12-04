# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 02:50:18 2019

@author: Diego Campanini
"""
#%%
import estructura 
from lista import *

#%% c3 2014-2 p2
estructura.crear('par','curso1 curso2')
class Catalogo:
    def __init__(self):
        self.__pares=[]
    
    def requisitos(self,curso):
        largo=len(self.__pares)
        arrReq=[]
        for i in range(largo):
            unpar=self.__pares[i]
            if unpar.curso2==curso:
                arrReq=arrReq+[unpar.curso1]
        return arrReq
    
    def agregar(self,curso2,listaReq):
        if listaReq==[]:
            unpar=par(None,curso2)
            self.__pares=self.__pares + [unpar]
            return
        for r in listaReq:
            unpar=par(r,curso2)
            self.__pares=self.__pares + [unpar]
        return
    
    def printCatalogo(self):
        return self.__pares


#%% p2 (b)
arrayRequi=[]
def todosLosRequisitos(curso,c):
    global arrayRequi
    req=c.requisitos(curso)
    arrayRequi=arrayRequi+req
    for uncurso in req:
        todosLosRequisitos(uncurso,c)
    # ordenar arreglo de menor a mayor
    arrayRequi.sort()
    # sacar None del arrayRequi
    newArr=[]
    for i in arrayRequi:
        if i!=None:
            newArr=newArr + [i]
    
    return newArr

#%% solucion pauta    
def todosLosRequisitos_pauta(curso,C): #0.1 encabezamiento
    L=C.requisitos(curso) #0.3 requisitos directos
    for req in L: 
        L=L+todosLosRequisitos(req,C) 

    L.sort() #0.2 ordenar ascendentemente
    return L

#%% crear y rellenar catalogo
c=Catalogo()
c.agregar('cc1002',[])
c.agregar('ma1101',[])
c.agregar('cc3001',['cc1002','ma1101'])
c.agregar('cc3002',['cc3001'])
print
print 'catalogo c= ', c.printCatalogo()

#%% probar todo los requisitos
print 
print 'todos los requisitos= ',todosLosRequisitos('cc3002',c)
    
    
#%%
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    