# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 02:45:22 2019

@author: Diego Campanini
"""

#%% c3 2017-2 p1
print 'Ingrese votos obtenidos por los candidatos'
g=input('votos gabriela? ')
j=input('votos jose? ')
r=input('votos rosa? ')
m=input('votos matias? ')
totalVotos=(g+j+r+m)
# calculo de porcentajes de votos para cada candidato
pGabi=100.0*g/totalVotos
pJose=100.0*j/totalVotos
pRosa=100.0*r/totalVotos
pMati=100.0*m/totalVotos
# armar arreglo con los porcentajes
percent=[pGabi,pJose,pRosa,pMati]

#%% funcion para encontrar el mayor de un arreglo
def mayor(array):
    m=array[0]
    for i in range(1,len(array)):
        if m < array[i]:
            m=array[i]
    return m
#%% funcion que saca el dado un elemento de un arreglo lo saca del arreglo
def sacar(array,m):
    newp=[]
    for i in range(len(array)):
        if m!=array[i]:
            newp=newp+[array[i]]
        else:
            newp=newp+array[i+1:]
            break
    return newp
    
#%% printear lo cadidatos de mayor a menor segun % de votos
print '\nResultados (en porcentaje):'
countGabi=0;countJose=0;countRosa=0;countMati=0
for i in range(len(percent)):
    m=mayor(percent)
    percent=sacar(percent,m)
    if m==pGabi and countGabi==0:
        countGabi=1 # lo hago para asegurar que print solo 1 vez gabi,
                    # si es que alguien mas tiene = cantidad de votos que gabi
        print 'Gabi ',pGabi
    elif m==pJose and countJose==0:
        countJose=1
        print 'Jose ',pJose
    elif m==pRosa and countRosa==0:
        countRosa=1
        print 'Rosa ',pRosa
    elif m==pMati and countMati==0:
        countMati=1
        print 'Mati ',pMati
        

# ============================================================================
# ============================================================================
#%% Pauta: Solución2. Construyendo lista [votos,candidato]
#construir lista de [votos,nombre] y sumar votos: 3.5 ptos
candidatos=['Gabriela','José','Rosa','Matias']
votosNombres=[] #0.3
suma=0 #0.2
for nombre in candidatos: #0.5
    pregunta='Votos '+nombre+'?' #0.5
    votos=input(pregunta) #0.2
    votosNombres.append([votos,nombre]) #1.5
    suma += votos #0.3
#mostrar resultados ordenados por porcentajes: 2.5 ptos
votosNombres.sort() #0.3 ordenar por votos
votosNombres.reverse() #0.2 de mayor a menor
for lista in votosNombres: #1.0
    porcentaje=100.0*lista[0]/suma #0.5
    print lista[1], porcentaje #0.5
        

#%%









































