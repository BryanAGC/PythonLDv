"""
Escribe una función que genere una lista de números primos hasta un número dado.
"""
def generar_primos(hasta):
    primos = []
    for num in range(2, hasta + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primos.append(num)
    return primos

# Ejemplo de uso
numero = 30
resultado = generar_primos(numero)
print(f"Los números primos hasta {numero} son: {resultado}")
