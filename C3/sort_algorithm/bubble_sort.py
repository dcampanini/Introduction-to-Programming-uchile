# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 02:36:19 2019

@author: Diego Campanini
"""

#%%
def ordenarBurbuja(datos):
    n1 = len(datos) # Se determina el largo
    n2 = n1
    for i in range(n1) :
        posMayor = 0 # Se toma el índice del primero (0)
        for j in range(n2)[1:n2]: # Se compara desde el segundo (1) hasta n2-1
            if datos[j] > datos[posMayor] : # Si es mayor, se cambia el índice
                posMayor = j
        # Finalizada la iteración, se cambia el mayor por el ultimo (n2-1)
        aux = datos[n2 - 1]
        datos[n2 - 1] = datos[posMayor]
        datos[posMayor] = aux
        # Dado que el último ha sido ordenado, se “acorta” el rango de búsqueda
        n2 = n2 - 1
    return datos

#%%
a=[4,54,64,7,1,102,10]
print
print 'original array=',a
ordenarBurbuja(a)
print 'sort array=', a