"""
Calcula la mediana de los elementos de una matriz 3x3.
"""
import numpy as np

matriz = np.random.randint(1, 100, (3, 3))
mediana = np.median(matriz)
print("Matriz:\n", matriz)
print("Mediana:", mediana)
