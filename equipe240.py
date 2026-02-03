print('hello world')

import numpy as np
import matplotlib.pyplot as plt
from suiteSn import suiteSn

# 1.2 Exercices:
a = np.full((6, 1), 1) # ok
b = np.arange(7) # ok
c = a.reshape(6) # ok
d = c * 240 # ok
I = np.identity(6) # ok
J = np.full((6, 6), 1) # ok
K = np.diag(b) # ok
L = I * 55 - J + 2*(a*c) # ok (vérifié à quoi est supposé ressembler la matrice)
M = K
M[:, 0] = a.reshape((6,1))
print(M)