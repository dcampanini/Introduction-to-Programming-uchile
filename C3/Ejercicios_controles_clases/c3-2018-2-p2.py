# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:22:17 2019

@author: Diego Campanini
"""

#%% c3 2018-2 p2
class conjunto:
    def __init__(self,unConjunto):
        self.__lista=unConjunto
            
    def complemento(self):
        # conj es el conjunto al que se le va a determinar el complemento
        conj=self.__lista 
        c_complemento=range(1,101)
        for elemento in conj:
            for i in range(len(c_complemento)):
                # si un elemento del conjunto esta en el c_complemento lo saco
                if elemento==c_complemento[i]:
                    c_complemento=c_complemento[:i]+c_complemento[i+1:]
                    break
        return c_complemento
    
    def cardinal(self):
        conj=[]
        for i in range(len(self.__lista)):
            if self.__lista[i]==True:
                conj=conj+[i+1]
        
        return len(conj)
                

#%%
c=conjunto([3,4,2])
print 
print 'c complemento= ', c.complemento()
cbool=conjunto([False,True,True,True,False,False])
print
print 'cbool cardinal= ',cbool.cardinal()

    
#%%
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

























    
        