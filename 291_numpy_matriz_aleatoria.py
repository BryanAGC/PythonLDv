"""
Crea una matriz 5x5 con números enteros aleatorios entre 1 y 100.
"""
import numpy as np

matriz = np.random.randint(1, 101, (5, 5))
print(matriz)
