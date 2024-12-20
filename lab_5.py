#implementar dtft numérica e testar nos sinais
#retangulo
# impulso
# a^n u[n]

import numpy as np
import matplotlib.pyplot as plt
import pds

A = 1
L = 11
n = np.arange(-10, 21)
N = len(n)
x1 = np.zeros(N)
x1[(0 <= n) & (n <= L - 1)] = A


#primeiro sinal 

w, X1 = pds.dtft(n, x1)
plt.figure(1)
plt.plot(w, np.abs(X1))

#segundo sinal

x2 = pds.delta(n)
w, X2 = pds.dtft(n, x2)
plt.figure(2)
plt.plot(w, np.abs(X2))

#terceiro sinal

a =0.5
x3 = a**n * pds.u(n)
w, X3 = pds.dtft(n, x3)
plt.figure(3)
plt.plot(w, np.abs(X3))