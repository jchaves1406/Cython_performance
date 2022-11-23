"""
Autor: Jesús Chaves
Distancia euclideana todos con todos
Fecha 22 de noviembre 2022
Tema: Optimización en Cython
"""

import numpy as np
import euclidean_cy_V1
import euclidean_cy_V2
import euclidean_py
import time

n=0
for i in range(6):
    n += 500
    data = np.random.randn(n, 3)
    for i in range(30):
        ini_time = time.time()
        euclidean_py.distancia_pares(data)
        fin_time = time.time()
        python_time = fin_time - ini_time
        print(f"Python time: {python_time} segundos.")

        ini_time = time.time()
        euclidean_cy_V1.distancia_pares_cython_estatico(data)
        fin_time = time.time()
        cython_time_V1 = fin_time - ini_time
        print(f"Cython basico time: {cython_time_V1} segundos.")

        ini_time = time.time()
        euclidean_cy_V2.distancia_pares_cython(data)
        fin_time = time.time()
        cython_time_V2= fin_time - ini_time
        print(f"Cython final time: {cython_time_V2} segundos.")

        with open('euclidean_distance_01.csv', 'a') as archivo:
            archivo.write('\n{:.6f},{:.6f},{:.6f}'.format(python_time, cython_time_V1, cython_time_V2))