"""
Escribe una función que convierta un número decimal a su equivalente en binario.
"""
def decimal_a_binario(numero):
    return bin(numero)[2:]

# Ejemplo de uso
numero = 10
resultado = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {resultado}")
