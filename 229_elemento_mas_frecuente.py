"""
Escribe una función que reciba una lista y devuelva el elemento más frecuente.
"""
from collections import Counter

def elemento_mas_frecuente(lista):
    return Counter(lista).most_common(1)[0][0]

# Ejemplo de uso
lista = [1, 2, 2, 3, 4, 2, 5, 5, 5]
resultado = elemento_mas_frecuente(lista)
print(f"El elemento más frecuente es: {resultado}")
