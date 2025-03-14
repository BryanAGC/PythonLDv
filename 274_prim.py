"""
Escribe una función que determine si un número es primo.
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(es_primo(11))  # True
print(es_primo(10))  # False
