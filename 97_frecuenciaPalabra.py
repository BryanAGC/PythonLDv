"""
Dado un texto, cuenta la frecuencia de cada palabra y devuelve un diccionario con los conteos.
"""
from collections import Counter

def contar_palabras(texto):
    palabras = texto.lower().split()
    return dict(Counter(palabras))

# Ejemplo de uso
texto = "hola mundo hola a todos en el mundo"
print(contar_palabras(texto))  
# {'hola': 2, 'mundo': 2, 'a': 1, 'todos': 1, 'en': 1, 'el': 1}
#tss2