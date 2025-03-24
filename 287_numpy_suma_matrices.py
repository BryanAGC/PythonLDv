"""
Suma dos matrices 2x2 con valores aleatorios entre 0 y 10.
"""
import numpy as np

a = np.random.randint(0, 10, (2, 2))
b = np.random.randint(0, 10, (2, 2))
print("Matriz A:\n", a)
print("Matriz B:\n", b)
print("Suma:\n", a + b)
