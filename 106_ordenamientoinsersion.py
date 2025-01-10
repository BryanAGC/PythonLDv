"""
Implementa el algoritmo de ordenamiento por inserción.
"""
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ejemplo de uso
print(ordenamiento_insercion([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]
