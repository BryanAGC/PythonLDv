"""
Resuelve un sistema de ecuaciones lineales usando NumPy.
"""
import numpy as np

A = np.array([[2, -1], [1, 3]])
b = np.array([3, 7])
solucion = np.linalg.solve(A, b)

print("Solución del sistema:", solucion)
