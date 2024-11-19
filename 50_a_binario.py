"""
Escribe una función que reciba un número entero y devuelva su representación en binario como cadena.
"""
def a_binario(numero):
    return bin(numero)[2:]


print(a_binario(10))  # '1010'
print(a_binario(255))  # '11111111'
