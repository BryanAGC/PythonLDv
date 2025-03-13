"""
Escribe una función que reciba un número N y devuelva la suma de los primeros N números naturales.
"""
def suma_naturales(n):
    return sum(range(1, n + 1))

print(suma_naturales(10))
