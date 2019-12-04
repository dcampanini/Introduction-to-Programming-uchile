# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:37:41 2019

@author: Diego Campanini
"""
#%% funcion para calcular el promedio dada una linea
def promedioLinea(linea):
    n1=int(linea[0:2])
    n2=int(linea[3:5])
    return int((n1+n2)/2.0)

#%% abrir archivos y leer las lineas
archivo = open("notas.txt", "r")
# linea 1
linea1 = archivo.readline( )
p1=promedioLinea(linea1)
# linea 2
linea2 = archivo.readline( )
p2=promedioLinea(linea2)
# linea 3
linea3 = archivo.readline( )
p3=promedioLinea(linea3)
# linea 4
linea4 = archivo.readline( )
p4=promedioLinea(linea4)
# linea 5
linea5 = archivo.readline( )
p5=promedioLinea(linea5)

archivo.close()

#%% abrir y escribir en otro archivo
arch=open('notaFinal.txt','w')
arch.write(linea1[0:len(linea1)-1]+' '+str(p1)+'\n')
arch.write(linea2[0:len(linea2)-1]+' '+str(p2)+'\n')
arch.write(linea3[0:len(linea3)-1]+' '+str(p3)+'\n')
arch.write(linea4[0:len(linea4)-1]+' '+str(p4)+'\n')
arch.write(linea5[0:len(linea5)]+' '+str(p5)+'\n')
arch.close()

#%%

















































