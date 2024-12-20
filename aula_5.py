import numpy as np
import matplotlib.pyplot as plt
import pds

A = 1
L = 11
w = np.linspace(-np.pi, np.pi, 512)


X = A*np.exp(-1j*w*(L-1)/2)*np.sin(w*L/2)/np.sin(w/2)

# X = np.sin(w*L/2)/np.sin(w/2)

plt.figure(1)
plt.plot(w, np.abs(x))

a = .5
X =1/(1-a*np.exp(-1j*w))


# plt.figure(1)
# plt.plot(w, X)

n = np.arange(-20, 21)
wc = np.pi/4
x = pds.sinc(n, wc)

plt.figure(2)
plt.stem(n, x)


