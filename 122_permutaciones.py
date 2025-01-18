"""
Genera todas las permutaciones posibles de una cadena dada.
"""
from itertools import permutations

def generar_permutaciones(cadena):
    return [''.join(p) for p in permutations(cadena)]

# Ejemplo de uso
print(generar_permutaciones("abc"))








