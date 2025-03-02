"""
Escribe una función que calcule la suma de los primeros N números naturales.
"""
def suma_primeros_n(n):
    return sum(range(1, n + 1))

# Ejemplo de uso
n = 10
resultado = suma_primeros_n(n)
print(f"La suma de los primeros {n} números naturales es: {resultado}")
#