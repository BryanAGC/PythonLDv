"""
Crea una matriz 5x5 con un patrón: ceros en todas partes excepto en la diagonal secundaria que tendrá unos.
"""
import numpy as np

matriz = np.zeros((5, 5), dtype=int)
np.fill_diagonal(np.fliplr(matriz), 1)
print(matriz)
