"""
Normaliza un arreglo (media = 0, desviación estándar = 1).
"""
import numpy as np

arreglo = np.random.randn(10)
normalizado = (arreglo - np.mean(arreglo)) / np.std(arreglo)
print("Original:", arreglo)
print("Normalizado:", normalizado)
