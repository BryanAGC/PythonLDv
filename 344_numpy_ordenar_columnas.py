"""
Ordena cada columna de una matriz 5x5 de manera independiente.
"""
import numpy as np

matriz = np.random.randint(0, 100, (5, 5))
ordenada = np.sort(matriz, axis=0)

print("Matriz original:\n", matriz)
print("Columnas ordenadas:\n", ordenada)
