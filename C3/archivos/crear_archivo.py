# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:23:26 2019

@author: Diego Campanini
"""

#%% Open a file

archivo = open("miArchivo.txt", "w") # crear y abrir un archivo
print "Nombre del Archivo: ", archivo.name
print "Esta cerrado? : ", archivo.closed
print "Modo de apertura: ", archivo.mode

#%% escribir en el archivo
archivo = open("miArchivo.txt", "w")
archivo.write("Esta es una linea\n")
archivo.write("creando la segunda linea\n")
archivo.write("Y esta es tercera linea")
archivo.close( )

#%% leyendo el archivo linea por linea
archivo = open("miArchivo.txt", "r")
linea1 = archivo.readline( )
linea2 = archivo.readline( )
linea3 = archivo.readline( )
print linea1
print linea2
print linea3
archivo.close( )
#%% leer un linea 
archivo = open("miArchivo.txt", "r")
linea1 = archivo.readline( )
print "Largo: ", len(linea1)
print "Contenido: ", linea1
print "Sin \\n: ", linea1[0 : len(linea1) - 1]

#%% leer todo el archivo 
archivo = open("miArchivo.txt", "r")
lineas = archivo.read( )
print lineas
archivo.close( )

#%%











































