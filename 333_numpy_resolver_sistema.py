"""
Resuelve el sistema de ecuaciones:
3x + y = 9
x + 2y = 8
"""
import numpy as np

A = np.array([[3, 1],
              [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)

print("Solución del sistema:", x)
