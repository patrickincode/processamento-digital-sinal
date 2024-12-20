import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss

#transformada inversa usando frações parciais

b = np.array([6, -10, 2])
a = np.array([1, -3, 2])

r, p, k = ss.residuez(b, a)
