"""
Escribe una función que determine si una cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# Ejemplo de uso
cadena = "reconocer"
if es_palindromo(cadena):
    print(f"{cadena} es un palíndromo.")
else:
    print(f"{cadena} no es un palíndromo.")
