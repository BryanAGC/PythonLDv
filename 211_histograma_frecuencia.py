"""
Escribe una función que reciba una lista de números y devuelva un diccionario con la frecuencia de cada número en la lista.
"""
from collections import Counter

def histograma_frecuencia(lista):
    return dict(Counter(lista))

# Ejemplo de uso
lista = [1, 2, 2, 3, 3, 3, 4]
resultado = histograma_frecuencia(lista)
print(f"Histograma de frecuencia: {resultado}")
