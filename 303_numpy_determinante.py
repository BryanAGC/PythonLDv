"""
Calcula el determinante de una matriz 3x3.
"""
import numpy as np

matriz = np.random.randint(1, 10, (3, 3))
det = np.linalg.det(matriz)

print("Matriz:\n", matriz)
print("Determinante:", det)
