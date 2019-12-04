# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:16:01 2019

@author: Diego Campanini
"""

#%% p1 (a)
def rotacionParcial(lista):
    largo=len(lista)
    ultimo=lista[largo-1]
    if largo>=1:
        for i in range(largo-2,0,-1):
            lista[i+1]=lista[i]
    lista[1]=ultimo

#%% probar funcion
lista=['A','B','C','D','E','F']
print 
print 'lista original=',lista
#%%
rotacionParcial(lista)
print
print 'lista cambiada=',lista

#%% p2 (b)
L=['UC','UCon','U','Ant','CC','UCal','UE','OH','H','AI','E','Cur','Pal','Iq','Coq','CLoa']

#%%
def versus(lista):
    p=''
    ult=len(lista)-1
    for i in range(len(L)/2):
        p=p + lista[i]+'-'+ lista[ult]+ '   '
        ult=ult-1
    return p


#%% programa que muestra los enfrentamientos de las 15 semanas de torneo
for i in range(1,16,1):
    print 'semana '+ str(i) +': '+ versus(L)
    rotacionParcial(L)


#%% solucion pauta
n=len(L) #0.2
for semana in range(1,n): #0.5
    print 'semana', semana, ':' #0.3
    for i in range(n/2): #0.7
        print L[i] + '-' + L[n-1-i] #0.8
    rotacionParcial(L) #0.5

#%%










































