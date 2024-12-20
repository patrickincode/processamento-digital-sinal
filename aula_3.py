# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:40:50 2024

@author: PGROCHEWSKI
"""

import numpy as np
import matplotlib.pyplot as plt
import pds

a = np.array([1])


N = 100
n = np.arange(N)
w0 = np.pi/10
x_clean = np.cos(w0*n)
x_noisy = x_clean + np.random.randn(N)

#utilizando filto média movel NAO RECURSIVO
M = 40
b = np.ones(M+1)/(M+1)
y = pds.lfilter(b, a, x_noisy)

plt.figure(1)
plt.plot(n,x_clean,n,x_noisy)
plt.figure(2)
plt.plot(n,x_clean,n,y)

#utilizando filtro media movel recursivo
a = np.array([1,-1])
b = np.zeros(M + 2)
b[0] = 1/(M + 1)
b[-1] = -1/(M + 1)
y2 = pds.lfilter(b, a, x_noisy)

plt.figure(1)
plt.plot(n,x_clean,n,x_noisy)
plt.figure(2)
plt.plot(n,x_clean,n,y2)

print(pds.mse(y , y2))