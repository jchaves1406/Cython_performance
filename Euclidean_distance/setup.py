# Fichero para la creación del objeto compartido

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("euclidean_cy_V2.pyx"))

setup(ext_modules = exts)