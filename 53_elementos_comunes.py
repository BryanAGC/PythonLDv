"""
Escribe una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas.
"""
def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))

print(elementos_comunes([1, 2, 3], [2, 3, 4]))  # [2, 3]
