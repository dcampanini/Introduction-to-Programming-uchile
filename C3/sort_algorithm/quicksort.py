# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:14:34 2019

@author: Diego Campanini
"""

#%% quicksort
#particionar: list int int -> int
#particiona L entre ip e iu (devuelve indice de pivote)
#ej: particionar(lista,0,len(lista)-1)

def particionar(L,ip,iu):
    #elegir pivote (por ejemplo: el primero)
    pivote=L[ip]
    #repetir hasta que indices se superen
    i=ip+1
    j=iu #indices de <s y >=s
    while i<=j:
        #avanzar índice de menores
        while i<=j and L[i]<pivote: 
            i+=1
        #retroceder índice de mayores o iguales
        while i<=j and L[j]>=pivote: 
            j-=1
        #intercambiar menor con mayor
        if i<=j: 
            L[i],L[j]=L[j],L[i]
            i+=1 
            j-=1
    #pivote a su posición final
    L[ip]=L[j]
    L[j]=pivote
    return j

#%%

#quicksort: list int int -> None
#ordena L entre indices ip e iu
#ej: quicksort(lista,0,len(lista)-1)
def quicksort(L,ip,iu):
    #caso base(1 elemento
    if ip>=iu:
        return
    #particionar (y obtener indice de pivote
    i=particionar(L,ip,iu)	
    #ordenar 1ª parte
    quicksort(L,ip,i-1)
    #ordenar 2ª parte	
    quicksort(L,i+1,iu)


#%% ordenar un array
#a=[4,54,64,7,1,102,10]
a=[50,40,30,20,10]
print
print 'original array=',a
quicksort(a,0,len(a)-1)
print 'sort array=', a


#%%
  











































