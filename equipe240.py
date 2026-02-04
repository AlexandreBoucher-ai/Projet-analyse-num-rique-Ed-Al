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

#plt.matshow(N)
#plt.title('Figure 1')
# plt.show()  pour la faire apparaitre et sauvegarder. À supprimer après avoir sauvegarder l'image ?

# on défini la fonction
def func(x):
    return -(x**2 / 2) + np.exp(x) + np.sin(x)

# on défini x, et on l'appelle pour les ordonné du plot
x = np.linspace(0, 1, 101)
#plt.plot(x, func(x))
#plt.title('Figure 2')
# plt.show() idem pour faire apparaître l'image



# 2 c)
# array de 20 colonne (0 à 19) en x et le array issu de la fonction défini pour les y
#plt.plot(np.arange(20), suiteSn(19))
#plt.title('Figure 3')
#plt.xlabel('n')
#plt.ylabel('Sn')
#plt.show()



# 3 a)
# 1. Calcul de D
# innitialisation de D (avec D(0) où h = 10**-1)
# D(x) est l'approximation de la dérivé de f(x)
D = np.array((func(0 + 19**-1) - func(0))/ 10**-1)
# on va de h = 10**-2 à 10**-12
for i in range(2, 13):
    D = np.append(D, (func(10**-i) - func(0)) / 10**-i)

# 2. On crée un array de même nombre de colonne avec la valeur réel de Fprime, soit 2
# (calculer à la calculatrice)
Fp = np.full(12, 2)

# 3. On crée un nouveau array qui est l'erreur comise pour chaque h
# erreur comise = Fp - D en valeur absolue
Err = Fp - D

#4. on crée un array pour h
h = np.array(10**-1)
for i in range(2, 13):
    h = np.append(10**-i)

#5. On crée le plot de l'erreur en fonction de h
plt
