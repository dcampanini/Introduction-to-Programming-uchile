# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:27:26 2019

@author: Diego Campanini
"""

#%% definir clase carta
class carta:
    def __init__(self, unaCalle, unaCiudad, unPais):
        self.calle = unaCalle
        self.ciudad = unaCiudad
        self.pais = unPais

#%% funcion que recibe una linea del archivo direccion.txt y entrega un 
# arreglo con tres elemento: la direccion, la ciudad y el pais
def separarDatos(linea):
    arr=[0]*3
    p=0 # indice para guardar en el array arr
    k=0 # indice para ir separando la linea
    for i in range(len(linea)):
        if linea[i]==',':
            arr[p]=linea[k:i]
            k=i+1
            p=p+1
            if p==2:
                arr[p]=linea[k:]
                break
    return arr
            

#%% leer todo el archivo de direcciones
archivo = open("direccion.txt", "r")
lineas = archivo.read( )
print  '\n Todas las cartas del archivo: \n'
print lineas
arrayCartas=[] # arreglos donde se guardaran los objetos de la clase carta
p=0
for i in range(len(lineas)):
    if lineas[i]=='\n':
        linea=lineas[p:i]
        p=i+1
        direccion=separarDatos(linea)
        # crear un objeto de la clase carta
        unaCarta=carta(direccion[0],direccion[1],direccion[2])
        arrayCartas=arrayCartas + [unaCarta]
        
    elif i==len(lineas)-1:
        ultimaLinea=lineas[p:i+1]
        direccionFinal=separarDatos(ultimaLinea)
        # crear un objeto de la clase carta
        unaCarta=carta(direccionFinal[0],direccionFinal[1],direccionFinal[2])
        arrayCartas=arrayCartas + [unaCarta]

archivo.close( )

#%% en el array arrayCartas se guardaron las direcciones como objetos de la 
# clase carta

# acceder a una carta
print '\nInformacion de una carta \n'
print arrayCartas[0].calle
print arrayCartas[0].ciudad
print arrayCartas[0].pais


#%%














































