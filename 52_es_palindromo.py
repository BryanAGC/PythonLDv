"""
Escribe una función que reciba un número y devuelva True si es palíndromo y False en caso contrario.
"""
def es_palindromo(numero):
    cadena = str(numero)
    return cadena == cadena[::-1]


print(es_palindromo(121))  # True
print(es_palindromo(123))  # False
