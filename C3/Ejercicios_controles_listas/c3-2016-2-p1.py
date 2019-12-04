# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:54:00 2019

@author: Diego Campanini
"""

#%% c3 2016-2 p1
# p1 (a)
def menores(lista,x):
    c=0
    for p in lista:
        if p<x:
            c=c+1
    return c

# programa
lista=[50,30,70,20]
print 'menores a x= ',menores(lista,50)

#%% p1 (b)
def listaMenores(lista):
    largo=len(lista)
    a=[0]*len(lista)
    for i in range(largo):
        m=menores(lista,lista[i])
        a[i]=m
    return a

# programa
print
print 'lista cantidad de menores= ',listaMenores(lista)

#%% p1 (c)
def listaOrdenada(lista):
    largo=len(lista)
    sortLista=[0]*largo
    arrayMenores=listaMenores(lista)
    for i in range(largo):
        sortLista[arrayMenores[i]]=lista[i]
    return sortLista

# programa
print
print 'lista original= ',lista
print 'lista ordenada= ', listaOrdenada(lista)

#%%


















































