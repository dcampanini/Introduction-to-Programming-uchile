# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:51:57 2019

@author: Diego Campanini
"""
import estructura 
from lista import *
#%% c3-2017-1  p1
def my_votos_a_imprimir(votantes):
    a=0;b=0;c=0
    tipoA=['rn','udi','ri','ep']
    tipoB=['rd','ph','pp','ev','pl','pi']
    tipoC=['sp']
    for i in votantes:
        partidoVotante=i.partido
        for k in tipoA:
            if partidoVotante==k:
                a=a+1
                break
        for k in tipoB:
            if partidoVotante==k:
                b=b+1
                break
        if partidoVotante==tipoC[0]:
            c=c+1
    
    return [a,b,c]
#%% 
#persona: run(str) nombre(str) partido(str)
estructura.mutable('persona','run nombre partido')
p1 = persona('12345678-9','Juan Perez','sp') #ejemplo
p2 = persona('12345678-9','Juan Perez','ri')
p3 = persona('12345678-9','Juan Perez','ev')
p4 = persona('12345678-9','Juan Perez','pl')
p5 = persona('12345678-9','Juan Perez','spaaaa')

votantes=[p1,p2,p3,p4,p5]
cantidadVotantes=my_votos_a_imprimir(votantes)

# ===========================================================================
# ===========================================================================
#%% solucion pauta (mas corta, sin los for internos que use)
#votos_a_imprimir: list(persona) -> list(int)
def votos_a_imprimir(votantes):
    A=0; B=0; C=0
    #recorrer lista de votantes #0.5
    for persona in votantes: #o for i in range(len(votantes)):
        #votos tipo C: 1.0 ptos
        p=persona.partido #0.2 o p=votantes[i].partido
        if p == "sp": #0.3
            C += 1 #0.5 (incluye 0.1 de C=0)
        #votos tipo A: 1.5 ptos
        elif p in ["rn","udi","ri","rp"]: #1.0
            A += 1 #0.5 (incluye 0.1 de A=0)
        #votos tipo B: 1.5 ptos
        elif p in ["rd","ph","pp","ev","pl","pi"]: #1.0
            B +=1 #0.5 (incluye 0.1 de A=0)
    #devolver lista: 0.5
    return [A,B,C]

# probar funcion
cantidadVotantes=votos_a_imprimir(votantes)

#%%
    














































