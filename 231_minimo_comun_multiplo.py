"""
Escribe una función que calcule el Mínimo Común Múltiplo (MCM) de dos números.
"""
import math

def minimo_comun_multiplo(a, b):
    return abs(a * b) // math.gcd(a, b)

# Ejemplo de uso
a = 12
b = 18
resultado = minimo_comun_multiplo(a, b)
print(f"El Mínimo Común Múltiplo de {a} y {b} es: {resultado}")
