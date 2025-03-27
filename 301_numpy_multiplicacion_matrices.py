"""
Multiplica dos matrices 3x3 y muestra el resultado.
"""
import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))
C = np.dot(A, B)

print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Producto A * B:\n", C)
