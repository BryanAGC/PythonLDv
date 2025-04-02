"""
Crea una matriz aleatoria 5x5 y obtiene el valor máximo de cada fila.
"""
import numpy as np

matriz = np.random.randint(0, 100, (5, 5))
maximos = np.max(matriz, axis=1)

print("Matriz:\n", matriz)
print("Máximos por fila:", maximos)
