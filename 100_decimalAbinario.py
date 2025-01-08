"""
Convierte un número decimal en su representación binaria sin usar bin().
"""
def decimal_a_binario(n):
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario or "0"

# Ejemplo de uso
print(decimal_a_binario(10))  # "1010"
