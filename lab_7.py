import pds
import numpy as np

N = 128
x = np.random.randn(N)

Xfft = np.fft.fft(x)
Xdft = pds.dft(x)

print(pds.mse(Xfft, Xdft))