import numpy as np
import matplotlib.pyplot as plt
import pds

#passa baixa com truncamento

M = 10

def filt(M):
    wc = np.pi/2
    m = np.arange(M+1)
    h = pds.sinc(m - M/2, wc)
    w = np.linspace( 0 , np.pi,  1024)
    w, H = pds.dtft(m, h, w)
    plt.plot( w, np.abs(H))
    plt.grid(True)
    return h
    

h = filt(100)
plt.legend(("10","20","40", "100"))

N = 100
n = np.arange(N)
w1 = np.pi / 20
w2 = 3 * np.pi / 4
x1 = np.cos(w1 *n)
x2 = np.cos(w2 *n)
x = x1 + x2
y = pds.lfilter(h, 1, x)
plt.figure()
plt.stem(n,x, "b") 
plt.stem(n,y, "r") 