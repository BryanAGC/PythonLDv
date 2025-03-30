"""
Genera una matriz 3x3 con números enteros aleatorios del 1 al 9 sin repetir.
"""
import numpy as np

arreglo = np.random.choice(np.arange(1, 10), size=(3, 3), replace=False)
print(arreglo)
