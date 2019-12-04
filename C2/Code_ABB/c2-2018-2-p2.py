# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:39:47 2019

@author: Diego Campanini
"""
# c2 2018-2 p2 
#%%
import estructura 
from lista import *

#%% primero se crea la estructura y el ABB con los que se va a trabajar
estructura.crear('libro','codigo titulo rutLector')
a=libro(10,'Python','12345678-K')#ejemplo1: libro 'Python' de código 10 prestado a RUT '12345678-K'
b=libro(20,'Python 3.0','') #ejemplo2: libro 'Python 3.0' de código 20 no está prestado
c=libro(30,'Java','87654321-0')#ejemplo3: libro 'Java' de código 30 prestado a RUT '87654321-0'

estructura.crear('arbol','valor izq der')
#libros de biblioteca en arbol binario de búsqueda según valores del código de los libros
bib=arbol(b,arbol(a,None,None),arbol(c,None,None)) #None es equivalente a arbolVacio
# crear segundo arbol
d=libro(5,'c++','')
e=libro(12,'hi python','')
bib2=arbol(b,arbol(a,arbol(d,None,None),arbol(e,None,None)),arbol(c,None,None))

#%% p2 a
def lector(c,bib):
    if bib==None:
        return 'libro no exite'
    elif c < bib.valor.codigo:
        return lector(c,bib.izq)
    elif c > bib.valor.codigo:
        return lector(c,bib.der)
    else: # c == bib.valor.codigo
        if bib.valor.rutLector !='':
            return bib.valor.rutLector
        else: # bib.valor.rutLector == ''
            return 'Libro disponible'

# programa
print
print 'Esta disponible un libro= ', lector(10,bib)

#%% funcion que concatena listas
estructura.crear('lista','valor siguiente')
def concatenar(l1,l2):
    return crearLista(l1,l2)
  
#%% funcion que busca libros con titulos que contengan la palaba p
# FUNCION CON ERRORES
#========================================================================
def myLibrosConPalabra(p,bib,lista=None):
    if bib.izq==None and bib.der==None:
        return bib.valor
    nodoRaiz=bib.valor
    nodoIzq=myLibrosConPalabra(p,bib.izq,lista)
    nodoDer=myLibrosConPalabra(p,bib.der,lista)
    print 
    #print 'raiz= ', nodoRaiz
    print
    print 'izq= ',nodoIzq
    print
    #print 'der= ',nodoDer
    print
    if nodoIzq!=None:
        if p in nodoIzq.titulo :
            lista=concatenar(nodoIzq,lista)
        if p in nodoRaiz.titulo :
            lista=concatenar(nodoRaiz,lista)
        if p in nodoDer.titulo:
            lista=concatenar(nodoDer,lista)
        return lista
    #if p in nodoIzq.titulo and p in nodoRaiz.titulo and p in  nodoDer.titulo:
        #lista=concatenar(nodoIzq,lista)
        #lista=concatenar(nodoRaiz,lista)
        #lista=concatenar(nodoDer,lista)
        #return 
#    elif p in nodoIzq.titulo and p in nodoRaiz.titulo:
#        lista=concatenar(nodoIzq,lista)
#        lista=concatenar(nodoRaiz,lista)
#        return lista
#    elif p in nodoIzq.titulo and p in nodoDer.titulo:
#        lista=concatenar(nodoIzq,lista)
#        lista=concatenar(nodoDer,lista)
#        return lista
#    elif p in nodoRaiz.titulo and p in nodoIzq.titulo:
#        lista=concatenar(nodoRaiz,lista)
#        lista=concatenar(nodoIzq,lista)
#        return lista
#    elif p in nodoRaiz.titulo and p in nodoDer.titulo:
#        lista=concatenar(nodoRaiz,lista)
#        lista=concatenar(nodoDer,lista)
#        return lista
#    elif p in nodoIzq.titulo and p in nodoDer.titulo:
#        lista=concatenar(nodoIzq,lista)
#        lista=concatenar(nodoDer,lista)
#        return lista
#    elif p in nodoIzq.titulo :
#        lista=concatenar(nodoIzq,lista)
#        return lista
#    elif p in nodoRaiz.titulo :
#        lista=concatenar(nodoRaiz,lista)
#        return lista
#    else:# p in nodoDer.titulo
#        lista=concatenar(nodoDer,lista)
#        return lista
#
#    


print
print'lista de libros con palabra p= ',myLibrosConPalabra('Python',bib,lista=None)
print # con el arbol bib2 la funcion anterior se cae
#print'lista de libros con palabra p en bib2= ',myLibrosConPalabra('Python',bib2,lista=None)

#=============================================================================
#=============================================================================


#%% solucion pauta

def librosConPalabra(palabra,bib):
    if bib==None: 
        return None #0.2
    L1=librosConPalabra(palabra,bib.izq) #0.4
    L2=librosConPalabra(palabra,bib.der) #0.4
    libro=bib.valor #0.2
    if palabra in libro.titulo: #0.3
        return concatenar(L1,lista(libro,L2)) #0.5
    else:
        return concatenar(L1,L2)

print
print 'libros = ', librosConPalabra('Python',bib)
print
print 'libros bib2 = ', librosConPalabra('Python',bib2)
#%%  
































#%%