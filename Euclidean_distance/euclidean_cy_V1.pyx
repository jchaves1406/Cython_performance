#cython: language_level=3
"""
Autor: Jesús Chaves
Distancia euclideana todos con todos
Fecha 22 de noviembre 2022
Tema: Optimización en Cython
"""

import cython
import numpy as np

# Por conveniencia podemos definir el tipo de data y dist con 

def distancia_pares_cython_estatico(double [:, ::1] data):
    # Definimos el tipo de N, D, dist y data
    cdef int N = data.shape[0]
    cdef int D = data.shape[1]
    dist = np.zeros(shape=(N, N), dtype=np.double)
    cdef double [:, ::1] dist_view = dist
    # También definimos los índices, se puede usar int o Py_ssize_t 
    cdef int i, j, k
    for i in range(N):
        for j in range(i+1, N):
            for k in range(D):
                dist_view[i, j] += (data[i, k] - data[j, k])**2
            dist_view[i, j] = np.sqrt(dist_view[i, j])
            dist_view[j, i] = dist_view[i, j]
    return dist