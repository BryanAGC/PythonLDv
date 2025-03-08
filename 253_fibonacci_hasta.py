def fibonacci_hasta(n):
    secuencia = [0, 1]
    while secuencia[-1] + secuencia[-2] < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

print(fibonacci_hasta(50))
