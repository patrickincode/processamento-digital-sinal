# LABORATÓRIO DE PDS REVERBERAÇÃO
#
# Utilizar:
# alpha = 0.7
# tau1 = 50ms
# tau2 = 100ms
# tau3 = 500ms
    
#
"""
Created on Thu Oct 24 17:59:44 2024

@author: PGROCHEWSKI
"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import pds

x = np.load("123test.npy")

#DADOS
fs = 8192                        # frequencia
t =1/fs                          # tempo
alpha = 0.7                      # alpha coeficiente de atenuação
print(t)
d1 = round(0.05/t)               # amostra na posição de 50ms
print(d1)
d2 = round(0.100/t)              # amostra na posição de 100ms
print(d2)
d3 = round(0.500/t)              # amostra na posição de 500ms


# REPRODUÇÃO EM 50MS

# PARAMETROS FILTRO
a1 = np.zeros(d1)
a1[0]= 1 
a1[-1] = -alpha
b1 =np.array([1])
# FILTRO
y1 = pds.lfilter(b1, a1, x)     
# PLAY
sd.play(y1, fs, blocking= True)

#REPRODUÇÃO EM 100MS

# PARAMETROS FILTRO
a2 = np.zeros(d2)
a2[0]= 1 
a2[-1] = -alpha
b2 =np.array([1])

# FILTRO
y2 = pds.lfilter(b2, a2, x)
# PLAY
sd.play(y2, fs, blocking= True)


#REPRODUÇÃO EM 500MS

# PARAMETROS FILTRO
a3 = np.zeros(d3)
a3[0]= 1 
a3[-1] = -alpha
b3 =np.array([1])
# FILTRO
y3 = pds.lfilter(b3, a3, x)
# PLAY
sd.play(y3, fs, blocking= True)