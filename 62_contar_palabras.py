"""
Escribe una función que reciba un texto y devuelva cuántas palabras tiene.
"""
def contar_palabras(texto):
    return len(texto.split())

# Ejemplo de uso
print(contar_palabras("Hola, esto es un ejemplo de conteo de palabras."))  # 8
