"""
Crea una matriz 6x6 de números aleatorios entre 0 y 1, y calcula su media.
"""
import numpy as np

matriz = np.random.rand(6, 6)
media = np.mean(matriz)

print("Matriz:\n", matriz)
print("Media:", media)
