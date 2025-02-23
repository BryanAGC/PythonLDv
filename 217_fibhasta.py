"""
Escribe una función que genere la secuencia de Fibonacci hasta un número dado.
"""
def fibonacci_hasta(numero):
    secuencia = [0, 1]
    while secuencia[-1] + secuencia[-2] <= numero:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# Ejemplo de uso
numero = 100
resultado = fibonacci_hasta(numero)
print(f"La secuencia de Fibonacci hasta {numero} es: {resultado}")
