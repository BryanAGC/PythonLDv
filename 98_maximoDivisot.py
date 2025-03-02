"""
Calcula el Máximo Común Divisor (MCD) de dos números utilizando el algoritmo de Euclides.
"""
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Ejemplo de uso
print(mcd(48, 18))  # 6
#t