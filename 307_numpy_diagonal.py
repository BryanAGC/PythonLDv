"""
Extrae la diagonal principal de una matriz 5x5.
"""
import numpy as np

matriz = np.random.randint(1, 50, (5, 5))
diagonal = np.diag(matriz)

print("Matriz:\n", matriz)
print("Diagonal principal:", diagonal)
