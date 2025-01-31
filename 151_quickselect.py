"""
Implementa QuickSelect para encontrar el k-ésimo elemento más grande en un array.
"""
import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivote = random.choice(arr)
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    if k <= len(mayores):
        return quickselect(mayores, k)
    elif k <= len(mayores) + len(iguales):
        return pivote
    else:
        return quickselect(menores, k - len(mayores) - len(iguales))

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(quickselect(arr, k))  # 7
