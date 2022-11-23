
"""
Autor: Jesús Chaves
Distancia euclideana todos con todos
Fecha 22 de noviembre 2022
Tema: Optimización en Cython
"""

import numpy as np

# Distancia euclideana puro Python
def distancia_pares(data):    
    N, D = data.shape
    dist = np.zeros(shape=(N, N))
    for i in range(N):
        for j in range(i+1, N):
            for k in range(D):
                dist[i, j] += (data[i, k] - data[j, k])**2
            dist[i, j] = np.sqrt(dist[i, j])
            dist[j, i] = dist[i, j]
    return dist

# Distancia euclideana con ayuda de numpy       
def distancia_pares_numpy(data):
    return np.sqrt(np.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))