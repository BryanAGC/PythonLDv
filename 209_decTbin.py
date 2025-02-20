"""
Escribe una función que convierta un número decimal a binario.
"""
def decimal_a_binario(numero):
    return bin(numero)[2:]

# Ejemplo de uso
numero = 42
resultado = decimal_a_binario(numero)
print(f"{numero} en binario es: {resultado}")
