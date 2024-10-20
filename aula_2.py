# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:45:27 2024

@author: PGROCHEWSKI
"""

import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(-10,31) #intervalo
w0 = np.pi/10 #frequencia
# phi = -np.pi/3 #fase
A = 1 #amplitude
x = A*np.sin(w0*n)*pds.u(n)
# x = n**2
plt.figure()
plt.stem(n,x)


# y = x*(n) - x*(n-1)
y1 = x.copy()
y1[1:] -= x[:-1]

b = np.array([1,-1]) #h
a = np.array([1])
y2  = pds.eqdif(b, a, x)


plt.figure()
plt.stem(n,y1)
