"""
Cuenta la frecuencia de cada palabra en un texto dado.
"""
from collections import Counter

def frecuencia_palabras(texto):
    palabras = texto.lower().split()
    return Counter(palabras)

# Ejemplo de uso
texto = "Hola mundo hola Python mundo"
print(frecuencia_palabras(texto))
