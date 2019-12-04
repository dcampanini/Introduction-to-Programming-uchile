# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:53:53 2019

@author: Diego Campanini
"""

#%% crear diccionario
capitales = dict( )
capitales["Chile"] = "Santiago"
capitales["Francia"] = "Paris"
capitales["Peru"] = "Lima"
capitales
# acceder a todas las llaves
print
print 'keys=',capitales.keys()
# acceder a todas las definiciones
print 'definiciones=',capitales.values()
# acceder a una sola definicion mediante la llave
print 'Definicion de la llave Chile=',capitales['Chile']

#%%
print 'Santiago' in capitales
print 'Chile' in capitales

#%% agregar una definicion y luego cambiarla
capitales['Bolivia']='La Paz'
print
print 'capitales =', capitales
capitales['Bolivia']='Sucre'
print
print 'capitales cambiada=',capitales

#%% recorrer las llaves con un for
for pais in capitales:
    print 'La capital de', pais,'es',capitales[pais]




#%%


































