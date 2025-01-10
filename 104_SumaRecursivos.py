"""
Suma los dígitos de un número de forma recursiva hasta obtener un solo dígito.
"""
def suma_digitos(n):
    if n < 10:
        return n
    return suma_digitos(sum(int(d) for d in str(n)))

# Ejemplo de uso
print(suma_digitos(9875))  # 2 (9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2)
