import numpy as np
from math import e

def suiteSn(n):
    # on innitialise un array 1 seul temer pour l'instant, S0
    S = np.array([e-1])
    # on veut construire un tableau de n+1 élément, donc i prend n valeur et il y aura n itération
    # doit commencer à 1 car sinon tout est décalé, et on donc donc ajouté +1 à n aussi
    for i in range(1, n+1):
        S = np.append(S, np.exp(1) - i * S[-1])
    return S
# vérifier si résultat est bon
