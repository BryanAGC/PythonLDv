"""
Escribe una función que determine si un número es primo.
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = 29
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")
