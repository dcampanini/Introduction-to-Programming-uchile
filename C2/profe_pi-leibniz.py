# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:42:16 2019

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

def Pi(epsilon) :
    k = 1 # valor de k al partir
    pik = 1 # valor de la serie cuando k vale 1
    return 4 * leibniz(k, pik, epsilon)


# cerca: num num -> num
# dado un valor de Pi en la iteracion k de la serie
# de leibniz, calcula el termino k+1
# de la serie de leibniz. Si (pik – pik+1) < epsilon
# retorna pik+1
def leibniz(k, pik, epsilon) :
    # se calcula el valor de k+1
    pikmas1 = pik + leibniz_kesimo(k+1)
    if cerca(pik, pikmas1, epsilon) :
        return pikmas1
    else :
        return leibniz(k+1, pikmas1, epsilon)












#%%
















