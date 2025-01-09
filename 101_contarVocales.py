"""
Cuenta el número de vocales en una cadena dada.
"""
def contar_vocales(cadena):
    return sum(1 for letra in cadena.lower() if letra in "aeiou")

# Ejemplo de uso
print(contar_vocales("Python es genial"))  # 5
