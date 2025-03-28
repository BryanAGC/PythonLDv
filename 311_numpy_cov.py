"""
Calcula la matriz de covarianza entre dos vectores de datos.
"""
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)

covarianza = np.cov(x, y)
print("Vector x:", x)
print("Vector y:", y)
print("Matriz de covarianza:\n", covarianza)
