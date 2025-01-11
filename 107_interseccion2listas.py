"""
Encuentra la intersección entre dos listas (elementos en común).
"""
def interseccion(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Ejemplo de uso
print(interseccion([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
