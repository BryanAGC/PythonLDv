"""
Dada una lista de números y un valor k, encuentra el k-ésimo elemento más grande.
"""
import heapq

def k_esimo_mayor(lista, k):
    return heapq.nlargest(k, lista)[-1]

# Ejemplo de uso
print(k_esimo_mayor([3, 1, 4, 1, 5, 9, 2, 6], 3))  # 4
