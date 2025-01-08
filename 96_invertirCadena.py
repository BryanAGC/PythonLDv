"""
Invierte una cadena sin usar slicing.
"""
def invertir_cadena(cadena):
    invertida = ""
    for char in cadena:
        invertida = char + invertida
    return invertida

# Ejemplo de uso
texto = "Python"
print(invertir_cadena(texto))  # "nohtyP"
