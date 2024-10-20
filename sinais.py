# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:36:07 2024

@author: PGROCHEWSKI
"""

import numpy as np
import matplotlib.pyplot as plt
import pds

# n = np.arange (-4,10)
# x = pds.delta(n)
# plt.stem(n,x)

# n = np.arange (-4,10)
# x = pds.u
# plt.stem(n,x(n))

#senoide discreta
n = np.arange(0,31) #intervalo
w0 = np.pi/10 #frequencia
phi = -np.pi/3 #fase
A = 1 #amplitude
x = A*np.cos(w0*n + phi)
plt.stem(n,x)

# #exponencial
# n = np.arange(0,31)
# x = (.9)**n
# plt.stem(n,x)

# #exponencial
# n = np.arange(0,31)
# x = (-.9)**n
# plt.stem(n,x)

# #adição de sinal
# x = lambda n: (pds.u(n)-pds.u(n-6))*(.9)**n
# n = np.arange(-6,10)
# plt.stem(n, x(n))

# #reversao temporal
# x = lambda n: (pds.u(n)-pds.u(n-6))*(.9)**n
# n = np.arange(-6,10)
# plt.stem(n, x(-n))

#deslocamento temporal
# x = lambda n: (pds.u(n)-pds.u(n-6))*(.9)**n
# n = np.arange(-6,10)
# plt.stem(n, x(n-3))