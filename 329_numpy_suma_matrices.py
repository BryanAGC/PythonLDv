"""
Crea dos matrices 3x3 y súmalas elemento a elemento.
"""
import numpy as np

A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))
C = A + B

print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Suma A + B:\n", C)
