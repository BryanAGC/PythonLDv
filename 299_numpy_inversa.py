"""
Invierte una matriz cuadrada 3x3.
"""
import numpy as np

matriz = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])
inversa = np.linalg.inv(matriz)
print("Matriz original:\n", matriz)
print("Matriz inversa:\n", inversa)
