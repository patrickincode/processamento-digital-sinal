import numpy as np
import matplotlib.pyplot as plt
import pds

w0 = np.pi/4
def H(w):
    return 1 - 2*np.cos(w0)*np.exp(-1j*w) + np.exp(-2j*w)

w = np.linspace(-np.pi, np.pi, 512)

plt.plot(w/np.pi, np.abs(H(w)))
plt.show()

