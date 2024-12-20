import numpy as np
import matplotlib.pyplot as plt
import pds

N = 100
n0 = 11
n = np.arange(-n0, N)
w0 = .1*np.pi
alpha = .8
beta = .2
Ax = 1
phi_x = 0

x = Ax * np.cos(w0*n + phi_x)

def H (w):
    return beta / (1- alpha * np.exp(-1j * w))

Ay = Ax * np.abs(H(w0))
phi_y = phi_x + np.angle(H(w0))

ya =  Ay * np.cos(w0*n + phi_y) #analitico
b = np.array([beta]) #numerico
a = np.array([1, -alpha])
yn = pds.lfilter(b, a, x)

plt.plot(n[n0:], x[n0:], n[n0:] ,ya[n0:] , n[n0:] , yn[n0:])
plt.show()