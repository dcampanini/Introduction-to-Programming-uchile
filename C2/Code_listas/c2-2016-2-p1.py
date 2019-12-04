# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 00:59:43 2019

@author: Diego Campanini
"""

#%% p1
import estructura 
from lista import *

estructura.crear('curso','codigo uds')
c1=curso('cc1000',5)
c2=curso('cc1002',10)
listaCursos1=crearLista(c1,crearLista(c2,None))

c10=curso('cc1000',15)
c20=curso('cc1002',10)
listaCursos2=crearLista(c10,crearLista(c20,None))

estructura.crear('alumno','nombre cursosInscritos')
a1=alumno('ana',listaCursos1)
a2=alumno('claudia',listaCurso2)

# lista de alumnos
alumnos=crearLista(a1,crearLista(a2,None))


#%% funcion para contar el numero de Uds dado una lista con los cursos inscritos
def numeroUds(cursos):
    if cursos==None:
        return 0
    else:
        return cabeza(cursos).uds + numeroUds(cola(cursos))

# probar funcion
print
print 'numeroUds=',numeroUds(listaCursos2)

#%% funcion que entrega el estudiante con mas uds
def alumnoMasUds(L,masUds=0):
    if cola(L)==None:
        return masUds
    else:
        if numeroUds(cabeza(L).cursosInscritos)<= numeroUds(cabeza(cola(L)).cursosInscritos):
            masUds=cabeza(cola(L)).nombre
            return alumnoMasUds(cola(L),masUds)
        else:
            masUds=cabeza(L).nombre
            return alumnoMasUds(cola(L),masUds)

# probar funcion
print
print 'alumno con mas Uds =',alumnoMasUds(alumnos)














#%%