# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:48:55 2019

@author: Diego Campanini
"""
#%%
class prueba:
    def __init__(self,x=0,y=0,z=0):
        self.__x=x
        self.__y=y
        self.__z=z
    
    def get(self):
        return [self.__x,self.__y,self.__z]

#%% programa
p=prueba(1,2,3)
print
print '[x,y,z]= ', p.get()

#%%





















































        