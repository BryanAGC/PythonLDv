"""
Convierte un arreglo de números decimales a enteros.
"""
import numpy as np

floats = np.array([1.2, 2.8, 3.9, 4.1])
enteros = floats.astype(int)

print("Original:", floats)
print("Convertido a enteros:", enteros)
