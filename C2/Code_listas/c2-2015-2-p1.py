# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:51:32 2019

@author: Diego Campanini
"""

#%%
import estructura 
from lista import *

estructura.crear('triangulo','a b c')
t1=triangulo(7,7,7)
t2=triangulo(10,10,5)
t3=triangulo(3,4,5)
listaTriangulos=crearLista(t1,crearLista(t2,crearLista(t3,None)))

#%% parte a
def perimetro(t):
    return t.a+t.b+t.c

# probar
print
print 'perimetro=',perimetro(t1)

def tipo(T):
    a=T.a; b=T.b; c=T.c #opcional para usar nombres a, b y c
    if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a: #0.5 primero validar
        return 0 #0.1
    if a==b and a==c: #0.3 condicion de equilatero
        return 3 #0.1
    if a==b or a==c or b==c: #0.3 condicion de isosceles
        return 2 #0.1
    return 1

#probar
print
print 'triangulo tipo=',tipo(t2)

#%% parte b
def soloIsosceles(listaTriangulos):
    if listaTriangulos==None:
        return None
    else:
        if tipo(cabeza(listaTriangulos))==2:
            return crearLista(cabeza(listaTriangulos),soloIsosceles(cola(listaTriangulos)))
        else:
            return soloIsosceles(cola(listaTriangulos))

# probar
print
print 'lista solo isosceles=',soloIsosceles(listaTriangulos)

#%% parte c
def mayorPerimetro(listaTriangulos,mayor=None):
    if cola(listaTriangulos)==None:
        return mayor
    else:
        if perimetro(cabeza(listaTriangulos))>= perimetro(cabeza(cola(listaTriangulos))):
            mayor=cabeza(listaTriangulos)
            print
            print 'if = ', mayor
            return mayorPerimetro(cola(listaTriangulos),mayor)
        else:
            mayor=cabeza(cola(listaTriangulos))
            print
            print 'else = ',mayor
            return mayorPerimetro(cola(listaTriangulos),mayor)

# probar
print
print 'mayor perimetro=',mayorPerimetro(listaTriangulos)












#%%























