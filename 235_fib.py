"""
Escribe una función que genere una secuencia de Fibonacci hasta un número dado.
"""
def fibonacci(hasta):
    secuencia = [0, 1]
    while secuencia[-1] + secuencia[-2] <= hasta:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# Ejemplo de uso
hasta = 50
resultado = fibonacci(hasta)
print(f"La secuencia de Fibonacci hasta {hasta} es: {resultado}")
