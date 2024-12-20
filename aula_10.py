import numpy as np
import matplotlib.pyplot as plt
import math
import pds
import scipy.signal as ss

wp = .25*np.pi
ws = .5*np.pi
Ap = .1
As = 50
Dw = ws - wp
wc = (wp + ws)/2 

dp = (10**(Ap/20)-1)/(10**(Ap/20)+1)
ds = 10**(-As/20)
d = min(dp, ds)
A = -20*np.log10(d)

print(f"A = {A} dB")

#hamming

L = 6.6*np.pi/Dw
M = math.ceil(L-1)
M +=  M % 2 #force M even 


m = np.arange(M+1)
hd = pds.sinc(m - M/2, wc)
win = ss.windows.hamming(M +1 )
h = win *hd

w, Hd = pds.dtft(m, hd , np.linspace(0, np.pi, 1024))
w, H = pds.dtft(m, h , np.linspace(0, np.pi, 1024))
plt.plot(w/np.pi, np.abs(Hd),w/np.pi, np.abs(H))

plt.grid(True)
plt.legend(("Hd", "H"))


