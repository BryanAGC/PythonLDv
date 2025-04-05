"""
Calcula la matriz de covarianza entre dos arrays.
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
covarianza = np.cov(x, y)

print("Matriz de covarianza:\n", covarianza)

