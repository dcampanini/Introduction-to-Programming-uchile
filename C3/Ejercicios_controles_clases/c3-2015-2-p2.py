# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:33:40 2019

@author: Diego Campanini
"""

#%% c3 2015-2 
# p2 (c)

class Dado:
    def __init__(self,lados):
        self.__lados=lados
        self.__valor=0
    
    def lanzar(self):
        import random 
        self.__valor=random.randint(1,self.__lados)
        return
    
    def valor(self):
        return self.__valor
#%% p2 (a)
# funcion para lanzar n dados 
def lanzarDados(n,lados):
    dados=[0]*n
    for i in range(n):
        d=Dado(lados) # crear objeto de la clase dado
        d.lanzar() # lanzar el dado d 
        dados[i]=d # guardar dado d en el array dados
    return dados

#%% p2 (b)
def valoresDados(listDados):
    valores=[0]*len(listDados)
    for i in range(len(listDados)):
        valores[i]=listDados[i].valor()
    valores.sort()
    valores.reverse()
    return valores

#%% p2 (c)

dadosPlayerA=lanzarDados(3,6) 
dadosPlayerB=lanzarDados(3,6)
valoresA=valoresDados(dadosPlayerA)
valoresB=valoresDados(dadosPlayerB)
print 'valores jugador A: ', valoresA
print 'valores jugador B: ', valoresB
# imprimir quien gana o empata si corresponde
if valoresA > valoresB:
    print 'gana jugador B'
elif valoresA < valoresB:
    print 'gana jugador A'
else:
    print 'empate'




#%%
    




















































