"""
Escribe una función que reciba un número entero y 
devuelva una lista con todos los números primos 
menores o iguales a ese número.
"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta(numero):
    return [n for n in range(2, numero + 1) if es_primo(n)]


numero = int(input("ingresa un numero"))
resultado = primos_hasta(numero)
print(f"Números primos menores o iguales a {numero}: {resultado}")
