"""
Escribe una función que reciba una cadena y devuelva el número de palabras que contiene.
"""
def contar_palabras(frase):
    return len(frase.split())

print(contar_palabras("Hola, ¿cómo estás hoy?"))
