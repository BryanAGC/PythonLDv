"""
Encuentra los índices de los elementos mayores que 10 en un arreglo.
"""
import numpy as np

arreglo = np.array([4, 12, 9, 15, 7, 20])
indices = np.where(arreglo > 10)
print("Índices:", indices)
