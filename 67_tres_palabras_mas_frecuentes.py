"""
Escribe una función que reciba un texto y devuelva las tres palabras más frecuentes en el texto, junto con sus conteos.
"""
from collections import Counter

def tres_palabras_mas_frecuentes(texto):
    palabras = texto.lower().split()
    contador = Counter(palabras)
    return contador.most_common(3)

print(tres_palabras_mas_frecuentes("python es genial y aprender python es divertido porque python es potente"))  

