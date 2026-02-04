print('hello world')

import numpy as np
import matplotlib.pyplot as plt
from suiteSn import suiteSn

# 1.2 Exercices:
a = np.full((6, 1), 1) # ok
#print(a)
b = np.arange(1, 7) # ok
#print(b)
c = a.reshape(6) # ok
#print(c)
d = c * 240 # ok
#print(d)
I = np.identity(6) # ok
#print(I)
J = np.full((6, 6), 1) # ok
#print(J)
K = np.diag(b) # ok
#print(K)
L = I * 55 - J + 2*(a*c) # ok (vérifié à quoi est supposé ressembler la matrice)
#print(L)
M = K ; M[:, 0] = a.reshape((6,)) # ok
#print(M)
dd = np.linalg.det(M) # ok
#print(dd)
x = np.linalg.solve(M, a) # ok (vérifié avec réponse attendu)
#print(x)
N = np.linalg.solve(M, M.T) # ok (M.T est un attribut (variable d'instance) des objet Numpy (la version transporté))
#print(N)

plt.matshow(N)
plt.title('matrice N')
plt.show() # pour la faire apparaitre et sauvegarder (déjà fait). À supprimer ?

def 