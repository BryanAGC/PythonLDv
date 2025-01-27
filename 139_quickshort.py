"""
Implementa Quicksort para ordenar una lista de números.
"""
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

# Ejemplo de uso
print(quicksort([3, 6, 8, 10, 1, 2, 1]))
