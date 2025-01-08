"""
Verifica si una cadena de texto es un palíndromo (se lee igual de izquierda a derecha y viceversa).
"""
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

# Ejemplo de uso
print(es_palindromo("Anita lava la tina"))  # True
