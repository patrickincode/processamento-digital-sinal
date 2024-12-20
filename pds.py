"""
modulo de processamento digital de sinal
"""
import numpy as np
from scipy.signal import lfilter

def u(n):
    return 1.*(n>=0)

def delta(n):
    return 1.*(n==0)

def eqdif(b, a, x):
    y = np.zeros_like(x)
    
    for n in range(len(y)): #laço para percorrer os valores de y
        for k in range(len(b)):
            m = n-k
            if m >=0:
                y[n] += b[k]*x[m]
        
        for k in range(1, len(a)):
            m = n-k
            if m >=0:
                y[n] -= a[k]*y[n-k]
                
    return y

def mse(x,y):
    return np.mean(np.abs(x-y)**2)
def sinc(n, wc=np.pi/4):
    # cl = [n!=0, n==0]
    # fl = [lambda n: np.sin(wc*n)/(np.pi*n), wc/np.pi]
    # return np.piecewise(n,cl,fl)
    x = np.sin(wc*n)/(np.pi*n)
    x [n==0] = wc/np.pi
    return x

# def dtft(n, x, w = np.linspace(-np.pi, np.pi, 512)):
#     K = len(w)
#     N = len(n)
#     X = np.zeros(K, dtype=complex)
#     for k in range(K):
#         for i in range(N):
#             X[k] += x[i]* (np.exp(-1j*w[k]*n[i]))
            

    
#     return  w, X

def dft(x):
    N = len(x)
    X  = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*np.exp(-2j/N * k * np.pi * n)
    
    return X

def mult(M, w, A):
    h = np.zeros(M + 1)
    n = np.arange(len(h))

        
    for k in range(len(A)):
        if(k == len(A) - 1):
            h[n] += A[k] * sinc(n - M/2, w[k])
            
        else:
            h[n] += ((A[k] - A[k+1]) * sinc(n - M/2, w[k]))

    return h

def fft(x):
    N = len(x)
    if N == 1:
        return x
    else:
        No2 = round(N/2)
        k = np.arange(No2)
        W = np.exp(-1j * 2 * np.pi / N)
        X = np.zeros(N, dtype=complex)
        Xe = fft(x[:-1:2])
        Xo = fft(x[1::2])

        X[k] = Xe + (W**k)*Xo
        X[k+No2] = Xe - (W**k)*Xo
    return X


def sinc2(m, wc):
    return np.piecewise(m, [m == 0], [wc/np.pi, lambda m: np.sin(wc*m)/(np.pi*m)])


def dtft(x, n=None, w=np.linspace(0, np.pi, 512)):
    N = len(x)
    K = len(w)
    n = n if n else np.arange(N)
    X = np.zeros(K, dtype=complex)
    for k in range(K):
        for i in range(N):
            X[k] += x[i]*np.exp(-1j*w[k]*n[i])
    return w, X


def multifaixa(w, A, L):
    h = np.zeros(L)
    m = np.arange(L)
    for k in range(len(w)-1):
        h += (A[k]-A[k+1])*sinc2(m - (L-1)/2, w[k])
    h += A[-1]*sinc2(m - (L-1)/2, w[-1])
    return h


