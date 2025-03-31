"""
Rota una matriz 3x3 90 grados en sentido horario.
"""
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rotada = np.rot90(matriz, -1)

print("Original:\n", matriz)
print("Rotada:\n", rotada)
