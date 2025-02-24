"""
Escribe una función que determine si un número es perfecto. Un número perfecto es aquel que es igual a la suma de sus divisores propios.
"""
def es_numero_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

# Ejemplo de uso
numero = 28
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
