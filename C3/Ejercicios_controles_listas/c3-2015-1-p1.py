# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 01:06:47 2019

@author: Diego Campanini
"""

#%% c3 2015-1 p1 (a)

def medallas(m,pais):
    listaNumber=[0]*3
    for p in m:
        if p[0]==pais:
            listaNumber[0]=p[1]
            listaNumber[1]=p[2]
            listaNumber[2]=p[3]
            return listaNumber
    return []

#%%
def lugar(m,pais):
    pos=1
    medalsPais=medallas(m,pais)
    # caso en que pais no esta en la lista
    if medalsPais==[]:
        return 0
    # caso en que pais si esta en la lista
    orosPais=medalsPais[0]
    for i in range(len(m)):
        otroPais=m[i][0]
        if pais!=otroPais:
            orosOtro=m[i][1]
            if orosOtro > orosPais:
                pos=pos+1
    return pos
    
#%% programa
m=[['argentina',14,29,31],['chile',5,6,18],['brasil',1,2,99]]
medals=medallas(m,'chile')
print
print 'medallas= ',medals
# determinar lugar
pos=lugar(m,'chile')
print
print 'lugar pais= ',pos


#%%














































