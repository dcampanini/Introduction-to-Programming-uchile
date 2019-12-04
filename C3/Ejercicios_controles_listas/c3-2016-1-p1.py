# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:38:18 2019

@author: Diego Campanini
"""
#%% c3 2016-1 p1
def diferenciaSimetrica(x,y):
    intersectados=[]
    # unir conjuntos
    unidos=x+y
    # intersectar x e y
    for i in x:
        if i in y:
            intersectados=intersectados + [i]
    # restar unidos y intersectados
    restados=[]
    for k in range(len(unidos)):
        if not unidos[k] in intersectados:
            restados=restados+[unidos[k]]
    
    return restados

#%%
#x=[1,2,3,4,5,6]
x=[3,1,2]
#y=[90, 91,92,2,5,6]
y=[2,1,4]
print 
print 'diferencia simetrica entre x e y= ', diferenciaSimetrica(x,y) 