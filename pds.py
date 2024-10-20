"""
modulo de processamento digital de sinal
"""
import numpy as np
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
    