import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(-3, 4)

plt.plot(n, pds.delta(n))
