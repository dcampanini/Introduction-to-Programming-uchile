# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 02:48:50 2019

@author: Diego Campanini
"""

#%% c3 2014-2 p1

def quitar(x,y):
    global unaLista
    if x>y:
        return 0
    elif x<y and x>=len(unaLista):
        return 0
    elif x<y and y<len(unaLista):
        eliminados=len(unaLista[x:y+1])
        first=unaLista[:x]
        second=unaLista[y+1:]
        unaLista=first+second
        return eliminados
    elif x<y and y>=len(unaLista):
        eliminados=len(unaLista[x:])
        unaLista=unaLista[:x]
        return eliminados
        


#%%
unaLista=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print
print 'unaLista antes= ',unaLista
eliminados=quitar(7,12)
print
print 'unaLista despues= ',unaLista, 'eliminados= ',eliminados