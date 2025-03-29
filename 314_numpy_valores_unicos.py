"""
Dado un arreglo con elementos repetidos, obtén los valores únicos.
"""
import numpy as np

arreglo = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unicos = np.unique(arreglo)

print("Valores únicos:", unicos)
