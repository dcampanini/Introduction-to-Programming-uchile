# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:38:17 2019

@author: Diego Campanini
"""
#%%
import estructura 
from lista import *

#%%
estructura.mutable("cartaMutable","calle ciudad pais")
miCartaMutable=cartaMutable("Lira 123","Stgo","Chile")
print
print 'miCartaMutable original= ',miCartaMutable

#%%
miCartaMutable.calle="Ahumada 222"
print
print 'miCartaMutable mutada= ',miCartaMutable
