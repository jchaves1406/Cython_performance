# Fichero para la creación del objeto compartido

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("linear_regression_cy.pyx"))

setup(ext_modules = exts)