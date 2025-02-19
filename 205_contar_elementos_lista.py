"""
Escribe una función que cuente el número total de elementos en una lista que puede contener otras listas dentro de ella.
"""
def contar_elementos(lista):
    return sum(len(item) if isinstance(item, list) else 1 for item in lista)

# Ejemplo de uso
lista = [1, [2, 3], 4, [5, 6], 7]
resultado = contar_elementos(lista)
print(f"El número total de elementos es: {resultado}")
