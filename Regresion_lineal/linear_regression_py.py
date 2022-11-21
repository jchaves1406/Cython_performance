"""
Autor: Jesús Chaves
Regresión Lineal, método de minimos cuadrados ordinarios
Fecha 22 de noviembre 2022
Tema: Optimización en Cython
"""

def least_sqares(x_values, y_values):
    '''
    Se implementa una función en Python la cual implementa el
    algoritmo de los minimos cuadrados sin usar ninguna biblioteca
    de las que se dispone en Python.

    Dado que la ecuación de una recta es y = mx + b se realiza una
    función para el calculo de la regresion lineal.
    '''
    N = len(x_values)
    x_mean = sum(x_values)/N
    y_mean = sum(y_values)/N
    variance_x, covariance_xy = 0, 0
    for x, y in zip(x_values, y_values):
        temp = x - x_mean
        variance_x += temp**2
        covariance_xy += temp * (y - y_mean)
    m = covariance_xy / variance_x
    b = y_mean - m*x_mean
    return (m, b)