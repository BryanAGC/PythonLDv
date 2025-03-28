"""
Transforma un arreglo de 16 elementos en una matriz 4x4.
"""
import numpy as np

arreglo = np.arange(1, 17)
matriz = arreglo.reshape((4, 4))
print(matriz)
