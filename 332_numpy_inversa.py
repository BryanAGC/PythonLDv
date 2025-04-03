"""
Calcula la inversa de una matriz 3x3 si es invertible.
"""
import numpy as np

matriz = np.array([[4, 7, 2],
                   [3, 6, 1],
                   [2, 5, 1]])

if np.linalg.det(matriz) != 0:
    inversa = np.linalg.inv(matriz)
    print("Inversa:\n", inversa)
else:
    print("La matriz no es invertible.")
