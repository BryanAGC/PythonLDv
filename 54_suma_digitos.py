"""
Escribe una función que reciba un número entero y devuelva la suma de sus dígitos.
"""
def suma_digitos(numero):
    return sum(int(digito) for digito in str(abs(numero)))


print(suma_digitos(123))  # 6
print(suma_digitos(-456))  # 15
