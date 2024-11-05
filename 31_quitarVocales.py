"""
Escribe una función que reciba una cadena de texto y devuelva la misma cadena pero con las vocales eliminadas.
"""

def eliminar_vocales(cadena):
    vocales = "aeiouAEIOU"  
    return ''.join(letra for letra in cadena if letra not in vocales)


cadena = "Hola Mundo"
resultado = eliminar_vocales(cadena)
print(f"Cadena sin vocales: '{resultado}'")
