"""
Concatena dos arreglos NumPy en uno solo.
"""
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
resultado = np.concatenate((a, b))
print(resultado)
