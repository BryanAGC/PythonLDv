"""
Crea una matriz 6x6 y rellena su diagonal principal con los valores [9,8,7,6,5,4].
"""
import numpy as np

matriz = np.zeros((6, 6), dtype=int)
np.fill_diagonal(matriz, [9, 8, 7, 6, 5, 4])

print(matriz)
