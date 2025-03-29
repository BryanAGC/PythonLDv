"""
Normaliza un arreglo (resta la media y divide entre la desviación estándar).
"""
import numpy as np

arreglo = np.random.randint(1, 100, 10)
media = np.mean(arreglo)
std = np.std(arreglo)
normalizado = (arreglo - media) / std

print("Original:", arreglo)
print("Normalizado:", normalizado)
