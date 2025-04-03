"""
Multiplica dos matrices compatibles: una 3x2 por una 2x4.
"""
import numpy as np

A = np.random.randint(0, 5, (3, 2))
B = np.random.randint(0, 5, (2, 4))
C = np.dot(A, B)

print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Producto A * B:\n", C)
