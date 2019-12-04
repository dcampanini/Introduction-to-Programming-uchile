# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:42:14 2019

@author: Diego Campanini
"""

#%%
import turtle

def fractal(n,L):
    lado(n,L) #0.3
    turtle.right(120) #0.3
    lado(n,L) #0.3
    turtle.right(120) #0.3
    lado(n,L)

def lado(n,L): #0.1
    if n==1: #0.2
        turtle.forward(L) #0.3
    else: #0.2
        turtle.left(60) #0.5
        lado(n-1,L/2) #0.3
        turtle.right(120) #0.5
        lado(n-1,L/2) #0.3
        turtle.left(120) #0.5
        lado(n-1,L/2) #0.3
        turtle.right(120) #0.5
        lado(n-1,L/2) #0.3
        turtle.left(60) #0.5