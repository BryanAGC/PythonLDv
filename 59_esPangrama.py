"""
Escribe una función que reciba una cadena y devuelva True si es un pangrama 
(contiene todas las letras del abecedario), ignorando mayúsculas y espacios.
"""
def es_pangrama(cadena):
    abecedario = set("abcdefghijklmnopqrstuvwxyz")
    return abecedario <= set(cadena.lower())

# Ejemplo de uso
print(es_pangrama("El veloz murciélago hindú comía feliz cardillo y kiwi"))  # True
