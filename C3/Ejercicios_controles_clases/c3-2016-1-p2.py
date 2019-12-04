# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:48:49 2019

@author: Diego Campanini
"""

#%%
class Cola:
    def __init__(self,n):
        self.__L=[]
        self.__capacidad=n
    
    def agregar(self,x):
         self.__L=self.__L+[x]
         return self.__L
     
    def valores(self):
        return self.__L
    
    def colar(self,x,y):
        if x in self.__L:
            print 'YaExiste'
            return
        if not y in self.__L:
            print 'NoExiste'
            return
        if self.__capacidad==len(self.__L):
            print 'ColaLlena'
            return
        # ahora se agregar x despues de y
        
        # lo siguiente esta incorrecto porque hay que modificar la cola original
        # ie self.__L no un nueva cola 
#        newCola=Cola(len(self.__L)-1)
#        for i in range(0,len(self.__L)):
#            print 
#            print 'inicio'
#            if self.__L[i]==y:
#                print
#                print 'holaaaaa'
#                newCola.agregar(x)
#                newCola.agregar(y)
#            else:
#                newCola.agregar(self.__L[i])
#        print newCola.valores()
        
        # forma correcta de proceder
        for i in range(len(self.__L)):
            if self.__L[i]==y:
                # guardar una parte del arreglo, desde y hasta el final
                resto=self.__L[i:]
                # ubicar x en la posicion de y
                self.__L[i]=x
                # concaternar el arreglo de 0 hasta x , mas el arreglo desde
                # y hasta el final y luego terminar porque ya se agrego x
                self.__L=self.__L[:i+1]+resto
                break
        
        return 
    

#%%
c=Cola(10)
# agregar elementos a la cola
c.agregar('a')
c.agregar('b')
c.agregar('c')
print
print 'valores cola= ', c.valores()
# colar la cola
c.colar('d','b')
print
print 'valores cola colada= ', c.valores()


#%%

















































