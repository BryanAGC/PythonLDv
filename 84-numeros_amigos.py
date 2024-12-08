"""
Determina si dos números son "números amigos". 
Dos números son amigos si la suma de los divisores propios de cada número es igual al otro número.
"""
def suma_divisores(n):
    return sum(i for i in range(1, n // 2 + 1) if n % i == 0)

def numeros_amigos(a, b):
    return suma_divisores(a) == b and suma_divisores(b) == a

print(numeros_amigos(220, 284))  # True
