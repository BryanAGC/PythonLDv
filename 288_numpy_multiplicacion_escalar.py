"""
Multiplica una matriz 3x3 por un escalar (por ejemplo, 5).
"""
import numpy as np

matriz = np.arange(1, 10).reshape(3, 3)
escalar = 5
resultado = matriz * escalar
print(resultado)
