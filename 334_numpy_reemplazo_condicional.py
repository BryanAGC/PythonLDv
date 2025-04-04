"""
Reemplaza los valores mayores a 50 por 999 en una matriz aleatoria 4x4.
"""
import numpy as np

matriz = np.random.randint(0, 100, (4, 4))
matriz[matriz > 50] = 999

print("Matriz modificada:\n", matriz)
