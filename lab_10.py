import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import pds  # Supondo que você já tenha o módulo pds.py com as funções sinc2, dtft e multifaixa implementadas.

# Especificações do filtro
delta = 0.001  # Ripple máximo
Dw = 0.01 * np.pi  # Largura máxima das faixas de transição

# Ganhos para cada faixa
G = [2, 4, 6, 3, 1]  

# Frequências de corte normalizadas
wc = [np.pi/5, 2*np.pi/5, 3*np.pi/5, 4*np.pi/5, np.pi]  

# Determina a ordem do filtro e o parâmetro beta
A = -20 * np.log10(delta)  # Atenuação em dB
L, beta = sig.kaiserord(A, Dw)
L += (L - 1) % 2  # Garante que L seja ímpar

# Geração do filtro utilizando multifaixa
h = pds.multifaixa(wc, G, L)

# Aplicação da janela Kaiser
h *= sig.get_window(("kaiser", beta), L)

# Cálculo da DTFT para análise do filtro
w, H = pds.dtft(h)

# Plot da resposta em frequência
plt.figure(figsize=(10, 6))
plt.plot(w / np.pi, np.abs(H), label="Filtro projetado")
plt.title("Resposta em frequência do filtro multifaixa")
plt.xlabel("Frequência normalizada (xπ rad/amostra)")
plt.ylabel("Magnitude")
plt.grid()
plt.legend()
plt.show()








