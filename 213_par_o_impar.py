"""
Escribe una función que determine si un número es par o impar.
"""
def par_o_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"

# Ejemplo de uso
numero = 7
resultado = par_o_impar(numero)
print(f"{numero} es {resultado}.")
