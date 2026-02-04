import numpy as np
from math import e

def suiteSn(n):
    # on innitialise un array 1 seul temer pour l'instant, S0
    S = np.array([e-1])
    # on veut construire un tableau de n+1 élément, donc i prend n valeur et il y aura n itération
    for i in range(n):
        S = np.append(S, np.exp(1) - n * S[-1])
    return S
    
print(suiteSn(10))