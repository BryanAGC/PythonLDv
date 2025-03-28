"""
Compara dos arreglos y muestra los elementos diferentes.
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 2, 4, 6])

diferentes = a != b
print("Elementos diferentes:", a[diferentes], b[diferentes])
