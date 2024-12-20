import numpy as np
import matplotlib.pyplot as plt
import pds
from time import time

NN = 11
N = 2 ** np.arange(NN)
mseLimit = 1e-13

tDFT = np.zeros(NN)
tFFT = np.zeros(NN)

for iN in range(NN):
    x = np.random.randn(N[iN])

    ti = time()
    XFFT = pds.fft(x)
    tFFT[iN] = time() - ti

    ti = time()
    XDFT = pds.dft(x)
    tDFT[iN] = time() - ti

    mse = pds.mse(XFFT, XDFT)
    if mse > mseLimit:
        raise ValueError(f"MSE between DFT and FFT is {mse}, grater than the limit {mseLimit}.")


plt.plot(N, tDFT, N, tFFT)
plt.legend(("DFT", "FFT"))
plt.xlabel("N")
plt.ylabel("Time [s]")
plt.title("Time of DFT vs FFT")
plt.grid(True)
plt.show()