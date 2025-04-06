"""
Aplica una función que eleva al cuadrado cada elemento de un array usando vectorize.
"""
import numpy as np

def cuadrado(x):
    return x ** 2

arr = np.array([1, 2, 3, 4, 5])
cuadrado_vectorizado = np.vectorize(cuadrado)(arr)

print("Array al cuadrado:", cuadrado_vectorizado)
