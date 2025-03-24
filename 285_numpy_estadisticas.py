"""
Dado un arreglo aleatorio de 10 elementos, encuentra su valor máximo, mínimo y promedio.
"""
import numpy as np

arreglo = np.random.randint(1, 100, 10)
print("Arreglo:", arreglo)
print("Máximo:", np.max(arreglo))
print("Mínimo:", np.min(arreglo))
print("Promedio:", np.mean(arreglo))
