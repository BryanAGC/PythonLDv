"""
Verifica si un número dado es una potencia de dos.
"""
def es_potencia_de_dos(n):
    return n > 0 and (n & (n - 1)) == 0

# Ejemplo de uso
print(es_potencia_de_dos(16))  # True
print(es_potencia_de_dos(18))  # False
