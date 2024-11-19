"""
Escribe una función que reciba un número entero y devuelva True si 
es un número perfecto. Un número perfecto es aquel que es igual a la suma de sus divisores propios.
"""
def es_perfecto(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    return sum(divisores) == numero


print(es_perfecto(28))  # True
print(es_perfecto(12))  # False
