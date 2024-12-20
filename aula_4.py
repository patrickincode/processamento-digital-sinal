# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:26:57 2024

@author: PGROCHEWSKI
"""

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 31)

w1 = 0 #[radiano/amostra]
x1 = np.cos(w1*n)
plt.figure(1)
plt.stem(n, x1)

w2 = 2*np.pi/20 #[radiano/amostra]
x2 = np.cos(w2*n)
plt.figure(2)
plt.stem(n, x2)

w3 = 2*np.pi/4 #[radiano/amostra]
x3 = np.cos(w3*n)
plt.figure(3)
plt.stem(n, x3)

w4 = 2*np.pi/2 #[radiano/amostra]
x4 = np.cos(w4*n)
plt.figure(4)
plt.stem(n, x4)

w5 = np.pi/10 + 6*2*np.pi #[radiano/amostra]
x5 = np.cos(w5*n)
plt.figure(5)
plt.stem(n, x5)