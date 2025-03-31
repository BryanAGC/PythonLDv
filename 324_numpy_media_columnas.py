"""
Calcula la media de cada columna en una matriz 4x4.
"""
import numpy as np

matriz = np.random.randint(0, 10, (4, 4))
media_columnas = np.mean(matriz, axis=0)

print("Matriz:\n", matriz)
print("Media por columnas:", media_columnas)
