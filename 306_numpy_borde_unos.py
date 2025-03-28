"""
Crea una matriz 6x6 de ceros con borde de unos.
"""
import numpy as np

matriz = np.zeros((6, 6), dtype=int)
matriz[0, :] = 1
matriz[-1, :] = 1
matriz[:, 0] = 1
matriz[:, -1] = 1
print(matriz)

