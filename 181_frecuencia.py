"""
Cuenta la frecuencia de palabras en un texto y las ordena de mayor a menor.
"""
from collections import Counter

def frecuencia_palabras(texto):
    palabras = texto.lower().split()
    frecuencia = Counter(palabras)
    return dict(sorted(frecuencia.items(), key=lambda x: -x[1]))

texto = "Este es un texto de ejemplo donde la palabra texto se repite varias veces"
print(frecuencia_palabras(texto))
