import numpy as np
import pds

# N = 8
# W = pds.dftmtx(N)

# n = np.arange(N)
# x = 5 + 2*np.cos(np.pi/2 * n)


# X =  W @ x


# np.set_printoptions(suppress=True)
# print(X)

# print(W @ np.conj(W)/N)


N = 12
W = pds.dftmtx(N)

n = np.arange(N)
x = 1 + 3*np.cos(np.pi/3 * n)+ np.sin(5*np.pi/6 *n)


X =  W @ x


np.set_printoptions(suppress=True)
print(X)