"""
Encuentra la posición (índice) del valor máximo en un arreglo 1D.
"""
import numpy as np

arr = np.array([1, 5, 20, 4, 10])
indice_max = np.argmax(arr)

print("Arreglo:", arr)
print("Índice del máximo:", indice_max)
