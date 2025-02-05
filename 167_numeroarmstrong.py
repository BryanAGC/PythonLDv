"""
Verifica si un número es un número de Armstrong.
"""
def es_armstrong(n):
    digitos = [int(d) for d in str(n)]
    return n == sum(d**len(digitos) for d in digitos)

print(es_armstrong(153))  # True
print(es_armstrong(9474))  # True
print(es_armstrong(123))  # False
