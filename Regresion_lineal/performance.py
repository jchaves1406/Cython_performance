import numpy as np
import linear_regression_cy
import linear_regression_py
import time
import random


n=0
for i in range(6):
    n += 1000000
    x = [x_i * random.randrange(8,12)/10 for x_i in range(n)]
    y = [y_i * random.randrange(8,12)/10 for y_i in range(n)]
    x_arr = np.asarray(x)
    y_arr = np.asarray(y)

    for i in range(30):
        ini_time = time.time()
        print(linear_regression_py.least_sqares(x_arr, y_arr))
        fin_time = time.time()
        python_time = fin_time - ini_time
        print(f"Python time: {python_time} segundos.")

        ini_time = time.time()
        print(linear_regression_cy.least_sqares(x_arr, y_arr))
        fin_time = time.time()
        cython_time = fin_time - ini_time

        print(f"Cython time: {cython_time} segundos.")


        print(f'Cython es {cython_time/python_time} mas rapido que python')

        with open('data_regression.csv', 'a') as archivo:
            archivo.write('\n{:.6f},{:.6f}'.format(python_time, cython_time))