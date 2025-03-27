"""
Ordena una matriz 4x4 de forma ascendente por filas.
"""
import numpy as np

matriz = np.random.randint(1, 100, (4, 4))
ordenada = np.sort(matriz, axis=1)

print("Original:\n", matriz)
print("Ordenada por filas:\n", ordenada)
