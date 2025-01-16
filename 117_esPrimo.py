"""
Verifica si un número es primo de manera optimizada.
"""
import math

def es_primo(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso
print(es_primo(97))  # True
print(es_primo(100))  # False
