import numpy as np
import matplotlib.pyplot as plt
import pds

A = np.array([1, 3, 5, 4, 2])
w = np.arange(1, 6) * np.pi / 5
M = 300
h = pds.mult(M, w, A)

m = np.arange(M)
w, H = pds.dtft(m, h, np.linspace(0, np.pi, 1024))

plt.plot(w/np.pi, np.abs(H))
plt.grid(True)
plt.title(f"M = {M}")

