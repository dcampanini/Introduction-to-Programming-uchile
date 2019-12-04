# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:39:30 2019

@author: Diego Campanini
"""
#%% clase polinomio

class Polinomio:
    def __init__(self,coef):
        self.__coeficientes=list(coef)
    
    # sumar dos polinomios
    def __add__(self,p):
        l1=len(self.__coeficientes)
        l2=len(p.__coeficientes)
        newPoli=[]
        
        if l1 == l2:
            for i in range(l1):
                newPoli=newPoli+[self.__coeficientes[i] + p.__coeficientes[i]]
        elif l1 < l2:
            self.__coeficientes=self.__coeficientes + [0]*(l2-l1)
            for i in range(l2):
                newPoli=newPoli+[self.__coeficientes[i] + p.__coeficientes[i]]
        else:
            p.__coeficientes=p.__coeficientes + [0]*(l1-l2)
            for i in range(l1):
                newPoli=newPoli+[self.__coeficientes[i] + p.__coeficientes[i]]
    
        return Polinomio(newPoli) 
        
    # representar los coeficiente como polinomio
    def __str__(self):
        cof=self.__coeficientes
        pol=''
        for i in range(len(cof)):
            pol=pol + str(cof[i]) + 'x^' + str(i) + '+'
        return pol[0:len(pol)-1]
    
    # metodo para derivar un polinomio
    def derivada1(self):
        # ojo que esta solucion no es tan buena porque es mejor crear un
        # arreglo con 0 y luego rellenarlo, que en cada iteracion ir aumentando
        # el tamaño de un intervalo
        polDerivado=[]
        for i in range(len(self.__coeficientes)):
            polDerivado=polDerivado + [self.__coeficientes[i]*i]
        return Polinomio(polDerivado[1:])
    
    # metodo para derivar pero sin hacer crecer en cada iteracion un arreglo
    def derivada(self):
        lenPol=len(self.__coeficientes)
        polDerivado=[0]*(lenPol-1)
        for i in range(lenPol)[1:]:
            polDerivado[i-1]=i*self.__coeficientes[i]
        return Polinomio(polDerivado)
    
    # metodo para evaluar un polinomio
    def eval(self,x):
        suma=0
        lenPol=len(self.__coeficientes)
        for i in range(lenPol):
            suma=suma+ self.__coeficientes[i]*(x**i)
        return suma
    
    
#%%
coeficientesA = [2, 5, -1, 8, 0, 4]
coeficientesB = [-3, 4, 0, 9]
pa = Polinomio(coeficientesA)
pb = Polinomio(coeficientesB)
pc=pa+pb
print
print 'pa=',str(pa)
print 'pa+pb=',str(pc)
pd=pc.derivada()
print 'pd=',str(pd)
valor=pd.eval(10)
print 'Derivada evaluada en 10:',valor


#%%




































