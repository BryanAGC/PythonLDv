"""
Verifica si una matriz cuadrada es simétrica.
"""
import numpy as np

matriz = np.array([[1, 2, 3],
                   [2, 4, 5],
                   [3, 5, 6]])

es_simetrica = np.array_equal(matriz, matriz.T)

print("Matriz:\n", matriz)
print("¿Es simétrica?:", es_simetrica)
