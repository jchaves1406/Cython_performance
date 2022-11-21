#cython: language_level=3

"""
Autor: Jesús Chaves
Regresión Lineal, método de minimos cuadrados ordinarios
Fecha 22 de noviembre 2022
Tema: Optimización en Cython
"""

cimport cython

@cython.boundscheck(False) 
@cython.wraparound(False)
@cython.cdivision(True)
cpdef least_sqares(x_values, y_values):
    '''
    Se implementa una función en Python la cual implementa el
    algoritmo de los minimos cuadrados sin usar ninguna biblioteca
    de las que se dispone en Python.

    Dado que la ecuación de una recta es y = mx + b se realiza una
    función para el calculo de la regresion lineal.
    '''
    cdef double x_mean, y_mean, variance_x, covariance_xy, m, b, temp
    cdef double[:] x = x_values
    cdef double[:] y = y_values
    cdef unsigned long N, i
    
    N = x.shape[0]
    x_mean = 0
    y_mean = 0
    for i in range(N):
        x_mean += x[i]
        y_mean += y[i]
    x_mean = x_mean/N
    y_mean = y_mean/N
    variance_x = 0
    covariance_xy = 0
    for i in range(N):
        temp = (x[i] - x_mean)
        variance_x += temp**2
        covariance_xy += temp*(y[i] - y_mean)
    m = covariance_xy / variance_x
    b = y_mean - m*x_mean
    return (m, b)