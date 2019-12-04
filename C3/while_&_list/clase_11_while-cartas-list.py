# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:45:36 2019

@author: Diego Campanini
"""

#%% while + cartas + list()
import estructura
estructura.crear('carta','calle ciudad pais')


cartas = list( )
c1 = carta('Lira 123', 'Santiago', 'Chile')
cartas = cartas + [ c1 ]
c2 = carta('Abaroa 2128', 'Calama', 'Chile')
cartas = cartas + [ c2 ]
c3 = carta('Vespucio 443', 'Arica', 'Chile')
cartas = cartas + [ c3 ]

#%% buscar una ciudad en la list de cartas y retornar True si esta o False si no
# my version
def my_estaLaCiudad(cartas,ciudad):
    for i in range(len(cartas)):
        if cartas[i].ciudad==ciudad:
            return True
    return False

print
print 'esta la ciudad: ',my_estaLaCiudad(cartas,'lama')

# version profe
def estaLaCiudad(cartas, ciudad):
    for cadaCarta in cartas : # se recorre toda la lista
        if cadaCarta.ciudad == ciudad:
            return True # se encontro
    return False # no esta la ciudad en la lista

print
print 'esta la ciudad: ',estaLaCiudad(cartas,'Calama')

#%% cuantas cartas tienen como destino un ciudad especifica
def contarCiudad(cartas,ciudad):
    c=0
    for cadaCarta in cartas:
        if cadaCarta.ciudad==ciudad:
            c=c+1
    return c

print
print 'contar la ciudad= ',contarCiudad(cartas,'Calama')

#%% crear nueva lista de cartas sin un ciudad especifica
def sacarCiudad(cartas,ciudad):
    new_cartas=[]
    for cadaCarta in cartas:
        if cadaCarta.ciudad!=ciudad:
            new_cartas=new_cartas+[cadaCarta]
    return new_cartas

print 
print 'lista original= ',cartas
print
print 'lista nueva= ',sacarCiudad(cartas,'Calama')
            
#%% indicar el numero de ciudades distintas que hay en la lista de cartas
def contarCiudadesDistintas(cartas):
    newCartas=[]
    for cadaCarta in cartas:
        unaCity=cadaCarta.ciudad
        if estaLaCiudad(newCartas,unaCity)==False:
            newCartas=newCartas+[cadaCarta]
    return len(newCartas)

print 
print 'numero de ciudades distintas en la lista= ',contarCiudadesDistintas(cartas)

#%% funcion que retorna la ciudad mas repetida de una lista
def contarUnaCiudad(cartas,ciudad):
    c=0
    for cadaCarta in cartas:
        unaCity=cadaCarta.ciudad
        if unaCity==ciudad:
            c=c+1
    return c
        
        
        
#%% funcion que entrega la ciudad mas repetida, si hay dos o mas entrega la
# primera que aparece en la lista 
def ciudadMasRepetida(cartas):
    city=cartas[0].ciudad
    c=contarUnaCiudad(cartas,city)
    masRepetida=city
    for cadaCarta in cartas:
        unaCity=cadaCarta.ciudad
        nc=contarUnaCiudad(cartas,unaCity)
        if c < nc:
            masRepetida=unaCity
            c=nc # actualizar c
    return masRepetida

# formar otra listas de cartas
newCartas=cartas+[c2]+[c2]
print
print 'newCartas= ',newCartas
print
print 'Ciudad mas repetida= ', ciudadMasRepetida(newCartas)
        
    
    
             

#%%



















































