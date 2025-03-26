"""
Dada una matriz 4x4, calcula la suma de cada fila y cada columna.
"""
import numpy as np

matriz = np.random.randint(1, 10, (4, 4))
suma_filas = np.sum(matriz, axis=1)
suma_columnas = np.sum(matriz, axis=0)

print("Matriz:\n", matriz)
print("Suma por filas:", suma_filas)
print("Suma por columnas:", suma_columnas)
