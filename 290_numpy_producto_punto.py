"""
Calcula el producto punto entre dos vectores NumPy de 3 elementos.
"""
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
producto_punto = np.dot(v1, v2)
print("Producto punto:", producto_punto)
