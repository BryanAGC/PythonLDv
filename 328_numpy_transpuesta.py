"""
Crea una matriz 3x4 y obtén su transpuesta.
"""
import numpy as np

matriz = np.arange(12).reshape(3, 4)
transpuesta = matriz.T

print("Matriz original:\n", matriz)
print("Transpuesta:\n", transpuesta)
