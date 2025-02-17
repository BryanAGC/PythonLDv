"""
Escribe una función que reciba un texto y devuelva la cantidad de veces que aparece cada palabra.
"""
from collections import Counter

def contar_palabras(texto):
    palabras = texto.split()
    return Counter(palabras)

# Ejemplo de uso
texto = "python es un lenguaje de programación y python es poderoso"
resultado = contar_palabras(texto)
print(resultado)
