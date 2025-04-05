"""
Encuentra los valores únicos en un array y cuántas veces se repite cada uno.
"""
import numpy as np

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
valores, conteos = np.unique(arr, return_counts=True)

print("Valores únicos:", valores)
print("Frecuencias:", conteos)
