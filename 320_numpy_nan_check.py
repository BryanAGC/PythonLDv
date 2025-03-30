"""
Comprueba si hay valores NaN (nulos) en un arreglo y cuántos hay.
"""
import numpy as np

arreglo = np.array([1, 2, np.nan, 4, np.nan])
hay_nan = np.isnan(arreglo)
cantidad = np.sum(hay_nan)

print("¿Hay NaN?:", hay_nan.any())
print("Cantidad de NaN:", cantidad)
