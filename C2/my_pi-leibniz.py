# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:54:53 2019

@author: Diego Campanini
"""
#%%
def esPar(x):
    if x%2==0:
        return True
    else:
        return False

# leibniz_kesimo: num -> num
# dado un valor de k, calcula el
# termino k de la serie de leibniz.
def leibniz_kesimo(k) :
    if esPar(k) :
        signo = -1
    else :
        signo = 1
    # se calcula el valor k-esimo
    # OJO 2.0 o 1.0 debe ser real!
    valor = signo * (1 / ((2.0 * k) - 1))
    return valor

# pi_Leibniz(n): int -> num
# calcula el numero pi hasta la iteracion k
def pi_Leibniz(k) :
    if (k == 1) :
        return 1
    else :
        # se calcula el valor k
        valorK = leibniz_kesimo(k)
        # se suma el valor a la serie y
        # se calcula los terminos faltantes
        return pi_Leibniz(k - 1) + valorK

# cerca: num num num -> bool
# retorna True si x es igual a y con
# precision epsilon
def cerca(x, y, epsilon) :
    diff = x - y
    return abs(diff) < epsilon

# calcular pi
def pi(eps,k=1,kmas1=2):
    pik=pi_Leibniz(k)
    pikmas1=pi_Leibniz(kmas1)
    if cerca(pik,pikmas1,eps):
        return 4*pikmas1
    else:
        return pi(eps,k+1,kmas1+1)




















