# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:41:46 2022

@author: wissa
"""

import matplotlib.pyplot as plt
import  json as js


fonction  = open ('loc.log')

f = js.load (fonction)

X=[]
for el in f:
 X.append(el[0])
 
Y=[]
for el in f:
 Y.append(el[1])
 
gp = plt.plot(X,Y)
plt.show ()
 