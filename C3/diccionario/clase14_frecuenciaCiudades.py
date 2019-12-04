# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:28:14 2019

@author: Diego Campanini
"""

#%% definir clase carta
class carta:
    def __init__(self, unaCalle, unaCiudad, unPais):
        self.calle = unaCalle
        self.ciudad = unaCiudad
        self.pais = unPais
#%% creando objetos de la clase carta
c1=carta('Lira 123','Santiago','Chile')
c2=carta('Abaroa 1280', 'Calama', 'Chile')
c3=carta('Ahumada 148', 'Quillota', 'Chile')
c4=carta('Piene 698', 'Calama', 'Chile')
c5=carta('Piene 698', 'Calama', 'Chile')
arrayCartas=[c1,c2,c3,c4,c5]

#%% funcion para contar cuantas veces se repite una ciudad
def cuantasVeces(cartas):
    cities=dict()
    count=1
    for c in cartas:
        unaCiudad=c.ciudad
        # si una ciudad esta en el diccionario se suma 1 al contador
        if unaCiudad in cities:
            count=count+1
            cities[unaCiudad]=count
        # si la ciudad no esta en el diccionario, se agrega
        else:
            cities[unaCiudad]=1
    # retornar el diccionario
    return cities

#%% 
print 
print cuantasVeces(arrayCartas)

#%%
    









































