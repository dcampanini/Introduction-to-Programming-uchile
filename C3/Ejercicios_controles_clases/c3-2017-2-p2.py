# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 01:59:38 2019

@author: Diego Campanini
"""
#%% c3 2017-2 p2
class redSocial:
    def __init__(self):
        self.__d={}
    
    def agregar(self,persona):
        self.__d[persona]=[]
        return self.__d
        
    def conectar(self,persona1,persona2):
        llaves=self.__d.keys()
        if persona1 in llaves and persona2 in llaves:
            # agregar persona2 a la lista de la persona1
            self.__d[persona1]=self.__d[persona1]+[persona2]
            # agregar persona1 a la lista de la persona2
            self.__d[persona2]=self.__d[persona2]+[persona1]
        
        return self.__d
    
    def conectados(self,persona1,persona2):
        llaves=self.__d.keys()
        # compruebo si una de las dos persona esta en la otra, ya que se 
        # asume que si una esta en otro, la otra igual estara en esa una, 
        # porque estan conectados
        if persona1 in self.__d[persona2]:
            return True
        return False
        


#%%
d1={'juan':['a','b'],'ana':['a','b','c']}
print 
print 'd inicial= ',d1
d1['juan']=d1['juan']+['ana']
print 'd actualizado= ',d1

#%% definir  objeto red social
r=redSocial()
# agregar una persona 
print
print 'agregar juan a la red social: ', r.agregar('juan')
print 'agregar ana a la red social: ',r.agregar('ana')
# conectar personas
print 'conectar ana con juan: ', r.conectar('ana','juan')
# preguntar si dos personas estan conectadas
print 'esta ana y juan conetados: ',r.conectados('ana','juan')



#%%






















































