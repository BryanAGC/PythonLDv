"""
Convierte un array 1D en una matriz diagonal.
"""
import numpy as np

arr = np.array([10, 20, 30, 40])
matriz_diagonal = np.diag(arr)

print("Matriz diagonal:\n", matriz_diagonal)
