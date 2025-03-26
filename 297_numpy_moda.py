"""
Encuentra el valor más frecuente (moda) en un arreglo.
"""
import numpy as np

arreglo = np.random.randint(0, 10, 20)
valores, conteos = np.unique(arreglo, return_counts=True)
moda = valores[np.argmax(conteos)]
print("Arreglo:", arreglo)
print("Moda:", moda)
