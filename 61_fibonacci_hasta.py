"""
Escribe una función que reciba un número entero y devuelva 
la secuencia de Fibonacci hasta ese número (sin incluirlo).
"""
def fibonacci_hasta(n):
    a, b = 0, 1
    resultado = []
    while a < n:
        resultado.append(a)
        a, b = b, a + b
    return resultado


print(fibonacci_hasta(20))  # [0, 1, 1, 2, 3, 5, 8, 13]
