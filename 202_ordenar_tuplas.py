"""
Escribe una función que reciba una lista de tuplas y ordene la lista por el segundo elemento de cada tupla.
"""
def ordenar_tuplas(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[1])

# Ejemplo de uso
tuplas = [(1, 3), (2, 1), (3, 2)]
resultado = ordenar_tuplas(tuplas)
print(resultado)
