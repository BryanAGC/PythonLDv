"""
Implementa el algoritmo de ordenamiento QuickSort usando el particionamiento de Lomuto.
"""
def quicksort(arr, inicio, fin):
    if inicio < fin:
        pivote = particion(arr, inicio, fin)
        quicksort(arr, inicio, pivote - 1)
        quicksort(arr, pivote + 1, fin)

def particion(arr, inicio, fin):
    pivote = arr[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

arr = [3, 6, 8, 10, 1, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)
