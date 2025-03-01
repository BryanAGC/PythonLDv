"""
Escribe una función que cuente cuántos elementos en una lista son mayores que un valor dado.
"""
def contar_mayores(lista, valor):
    return sum(1 for x in lista if x > valor)

# Ejemplo de uso
lista = [1, 5, 8, 2, 10, 3]
valor = 4
resultado = contar_mayores(lista, valor)
print(f"Hay {resultado} elementos mayores que {valor}.")
