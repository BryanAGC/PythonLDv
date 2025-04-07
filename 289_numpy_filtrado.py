"""
Dado un arreglo aleatorio, filtra los valores mayores que 50.
"""
import numpy as np

arreglo = np.random.randint(0, 100, 15)
print("Original:", arreglo)
filtrado = arreglo[arreglo > 50]
print("Mayores a 50:", filtrado)
