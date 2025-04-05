"""
Crea una matriz 2x2 y repítela en un mosaico 3x3 usando tile.
"""
import numpy as np

matriz = np.array([[1, 2],
                   [3, 4]])
mosaico = np.tile(matriz, (3, 3))

print("Mosaico 3x3:\n", mosaico)
