"""
Dado un arreglo aleatorio, filtra los valores mayores que 0.5.
"""
import numpy as np

arreglo = np.random.rand(20)
filtrados = arreglo[arreglo > 0.5]

print("Original:", arreglo)
print("Mayores que 0.5:", filtrados)
