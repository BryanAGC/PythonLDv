"""
Verifica si un número es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
def es_capicua(n):
    return str(n) == str(n)[::-1]

# Ejemplo de uso
print(es_capicua(12321))  # True
print(es_capicua(12345))  # False
