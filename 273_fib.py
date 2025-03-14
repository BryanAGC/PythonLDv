"""
Escribe una función que genere la secuencia de Fibonacci hasta el término N.
"""
def fibonacci(n):
    secuencia = [0, 1]
    for _ in range(n - 2):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

print(fibonacci(10))
