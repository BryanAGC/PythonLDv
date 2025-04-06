"""
Encuentra los elementos comunes entre dos arrays diferentes.
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
comunes = np.intersect1d(a, b)

print("Elementos comunes:", comunes)
