# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:17:46 2019

@author: Diego Campanini
"""

#%% c3 2015-1 
# p2 (b)
class Planilla:
    def __init__(self):
        self.__planilla={}
    
    def retornarPlantilla(self):
        return self.__planilla
    
    def set(self,celda,x):
        self.__planilla[celda]=x
        return self.__planilla
    
    def get(self,celda):
        if not celda in self.__planilla:
            return None
        else:
            return self.__planilla[celda]
#%% (a)
def trasponer(p):
    filas=range(1,27)
    columnas='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newP=Planilla()
    for i in filas:
        posfila=1
        for k in columnas:
            celda=k+str(i)
            v=p.get(celda)
            ponerFila=columnas[i-1] + str(posfila) # celda donde se va a poner el valor v
            posfila=posfila+1
            newP.set(ponerFila,v)
    
    return newP

#%% solucion de la pauta, hace lo mismo que la mia ie completa con None
# donde 
def trasponer2(P):
    Q=Planilla() #0.2
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #0.2
    for fila in range(1,27): #0.2
        for col in alfabeto: #0.2
            #trasponer valor: 2.0
            valor=P.get(col+str(fila)) #0.5
            filaQ=alfabeto.index(col)+1 #0.5
            colQ=alfabeto[fila-1] #0.5
            Q.set(colQ+str(filaQ),valor) #0.5
    return Q #

#%% (a) solucion 3, esta funcion entrega la plantilla traspuesta sin los None
# donde no hay un valor (como si pasa con las otras dos soluciones, 
# que rellenana con None, donde no hay nada)
def trasponer3(p):
    filas=range(1,27)
    columnas='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newP=Planilla()
    for i in filas:
        posfila=1
        for k in columnas:
            celda=k+str(i)
            v=p.get(celda)
            ponerFila=columnas[i-1] + str(posfila) # celda donde se va a poner el valor v
            posfila=posfila+1
            if v!=None:
                newP.set(ponerFila,v)
    
    return newP

#%% programa
p=Planilla()
# rellenar una fila 1
p.set('A1',1)
p.set('B1',2)
p.set('C1',3)
# rellenar fila 2
p.set('A2',4)
p.set('B2',5)
p.set('C2',6)
# rellenar fila 3
p.set('A3',7)
p.set('B3',8)
p.set('C3',9)
print 
print 'p= ', p.retornarPlantilla()
print 
print 'p traspuesta= ',trasponer3(p).retornarPlantilla()









#%%
    













































