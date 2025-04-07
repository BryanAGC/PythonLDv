"""
Reemplaza los valores negativos de un arreglo por ceros.
"""
import numpy as np

arreglo = np.array([5, -3, 7, -1, 0, 9])
arreglo[arreglo < 0] = 0
print(arreglo)
