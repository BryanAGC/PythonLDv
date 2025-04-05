"""
Normaliza un array 1D de números para que todos los valores estén entre 0 y 1.
"""
import numpy as np

arr = np.array([4, 8, 15, 16, 23, 42])
arr_norm = (arr - arr.min()) / (arr.max() - arr.min())

print("Array original:", arr)
print("Array normalizado:", arr_norm)
