"""
Verifica si un número es un número de Armstrong (la suma de sus dígitos elevados 
a la cantidad de dígitos es igual al número mismo).
"""
def es_armstrong(n):
    digitos = [int(d) for d in str(n)]
    return sum(d ** len(digitos) for d in digitos) == n

# Ejemplo de uso
print(es_armstrong(153))  # True
print(es_armstrong(9474))  # True
print(es_armstrong(123))  # False
